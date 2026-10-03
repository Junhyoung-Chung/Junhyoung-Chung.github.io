# frozen_string_literal: true
require 'yaml'
require 'uri'
require 'pathname'

module Materials
  ROOT = Pathname.new(__dir__).parent
  KINDS = ['Seminar slides', 'Poster', 'Lecture notes', 'Research paper'].freeze

  def self.read(path)
    match = path.read.match(/\A---\s*\n(.*?)\n---\s*(?:\n|\z)/m)
    raise ArgumentError, "#{path}: missing YAML front matter" unless match
    data = YAML.safe_load(match[1], aliases: false)
    raise ArgumentError, "#{path}: front matter must be a mapping" unless data.is_a?(Hash)
    data
  end

  def self.file_url!(value, root:, extension: nil)
    raise ArgumentError, 'Expected a URL string' unless value.is_a?(String) && !value.empty?
    raise ArgumentError, 'URLs cannot contain whitespace or backslashes' if value.match?(/[\s\\\x00-\x1f]/)
    uri = URI.parse(value)
    if value.start_with?('/') && !value.start_with?('//')
      decoded = URI::DEFAULT_PARSER.unescape(uri.path)
      raise ArgumentError, 'Unsafe local path' if decoded.split('/').include?('..') || decoded.include?('\\') || decoded.match?(/[\x00-\x1f]/)
      path = root.join(decoded.delete_prefix('/'))
      raise ArgumentError, "Missing local file: #{value}" unless path.file?
      raise ArgumentError, 'Local file escapes the site root' unless path.realpath.to_s.start_with?(root.realpath.to_s + '/')
      raise ArgumentError, "Expected a #{extension} file" if extension && path.extname.downcase != extension
    elsif uri.scheme != 'https' || !uri.host || uri.host.empty? || uri.userinfo
      raise ArgumentError, 'Use a root-relative local path or public HTTPS URL without credentials'
    end
    true
  rescue URI::InvalidURIError => error
    raise ArgumentError, error.message
  end

  def self.validate!(data, root: ROOT)
    %w[title kind pdf_url].each do |key|
      raise ArgumentError, "Missing #{key}" unless data[key].is_a?(String) && !data[key].strip.empty?
    end
    raise ArgumentError, "kind must be one of: #{KINDS.join(', ')}" unless KINDS.include?(data['kind'])
    raise ArgumentError, 'year must be a four-digit integer' unless data['year'].is_a?(Integer) && (1900..2100).cover?(data['year'])
    file_url!(data['pdf_url'], root: root, extension: '.pdf')
    file_url!(data['thumbnail'], root: root) if data['thumbnail']
    file_url!(data['source_url'], root: root) if data['source_url']
    true
  end
end
