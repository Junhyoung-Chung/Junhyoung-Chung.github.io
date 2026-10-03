#!/usr/bin/env ruby
# frozen_string_literal: true
require 'optparse'
require 'open3'
require 'fileutils'
require 'tmpdir'
require_relative 'materials'

options = { year: Time.now.year }
parser = OptionParser.new do |args|
  args.banner = 'Usage: ruby scripts/add_material.rb --file LOCAL.pdf --slug short-title --title TITLE --kind KIND [options]'
  args.on('--file PATH', 'Local PDF used to generate its first-page thumbnail') { |v| options[:file] = v }
  args.on('--slug SLUG', 'Lowercase words separated by hyphens') { |v| options[:slug] = v }
  args.on('--title TITLE') { |v| options[:title] = v }
  args.on('--kind KIND', Materials::KINDS, 'Seminar slides, Poster, Lecture notes, or Research paper') { |v| options[:kind] = v }
  args.on('--year YEAR', Integer) { |v| options[:year] = v }
  args.on('--venue TEXT') { |v| options[:venue] = v }
  args.on('--pdf-url URL', 'Public HTTPS original; omits the PDF from Git') { |v| options[:pdf_url] = v }
  args.on('-h', '--help') { puts args; exit }
end

begin
  parser.parse!
  %i[file slug title kind].each { |key| raise ArgumentError, "Missing --#{key}" unless options[key] }
  raise ArgumentError, 'Invalid slug' unless options[:slug].match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/)
  source = Pathname.new(options[:file]).expand_path
  raise ArgumentError, 'Input must be an existing PDF' unless source.file? && source.extname.downcase == '.pdf'
  root = Materials::ROOT
  record = root.join('_materials', "#{options[:slug]}.md")
  thumbnail = root.join('assets/thumbnails', "#{options[:slug]}.jpg")
  original = root.join('assets/materials', "#{options[:slug]}.pdf")
  [record, thumbnail, original].each { |path| raise ArgumentError, "Already exists (not overwritten): #{path}" if path.exist? }
  if options[:pdf_url]
    raise ArgumentError, '--pdf-url must use HTTPS' unless options[:pdf_url].start_with?('https://')
    Materials.file_url!(options[:pdf_url], root: root)
  elsif source.size > 20 * 1024 * 1024
    raise ArgumentError, 'For PDFs larger than 20 MiB, provide --pdf-url to keep the repository small.'
  end
  metadata = {'title' => options[:title], 'kind' => options[:kind], 'year' => options[:year]}
  metadata['venue'] = options[:venue] if options[:venue]
  raise ArgumentError, 'year must be a four-digit integer' unless (1900..2100).cover?(options[:year])
  raise ArgumentError, 'title cannot be blank' if options[:title].strip.empty?
  Dir.mktmpdir('material-thumbnail-') do |temp|
    target = File.join(temp, 'first-page')
    _stdout, stderr, status = Open3.capture3('pdftoppm', '-f', '1', '-singlefile', '-scale-to-x', '480', '-scale-to-y', '-1', '-jpeg', '-jpegopt', 'quality=82', source.to_s, target)
    raise ArgumentError, "PDF thumbnail failed: #{stderr}" unless status.success?
    image_path = "#{target}.jpg"
    raise ArgumentError, 'Thumbnail conversion produced no output' unless File.size?(image_path)
    thumbnail.dirname.mkpath
    record.dirname.mkpath
    FileUtils.cp(image_path, thumbnail)
    if options[:pdf_url]
      metadata['pdf_url'] = options[:pdf_url]
    else
      original.dirname.mkpath
      FileUtils.cp(source, original)
      metadata['pdf_url'] = "/assets/materials/#{original.basename}"
    end
    metadata['thumbnail'] = "/assets/thumbnails/#{thumbnail.basename}"
    Materials.validate!(metadata)
    record.write(YAML.dump(metadata) + "---\n\n")
  end
  puts "Added #{record.relative_path_from(root)} and #{thumbnail.relative_path_from(root)}"
  puts(options[:pdf_url] ? 'The PDF remains external; no PDF was copied into Git.' : "Local PDF: #{original.relative_path_from(root)}")
rescue ArgumentError, OptionParser::ParseError, Errno::ENOENT => error
  warn error.message
  warn 'Thumbnail generation requires Poppler (pdftoppm).'
  exit 1
end
