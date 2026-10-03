# frozen_string_literal: true
require 'tmpdir'
require_relative '../scripts/materials'

def rejects(message)
  begin
    yield
  rescue ArgumentError
    return
  end
  raise "Expected rejection: #{message}"
end

Dir.mktmpdir('materials-contract-') do |dir|
  root = Pathname.new(dir)
  root.join('notes.pdf').write('%PDF-1.7 test fixture')
  valid = {'title' => 'Lecture notes', 'kind' => 'Lecture notes', 'year' => 2026, 'pdf_url' => '/notes.pdf'}
  Materials.validate!(valid, root: root)
  Materials.validate!(valid.merge('pdf_url' => 'https://files.example.org/notes.pdf?version=2'), root: root)
  ['javascript:alert(1)', 'data:application/pdf;base64,abc', '//example.org/a.pdf', 'http://example.org/a.pdf', 'https://user:secret@example.org/a.pdf', '/%2e%2e/notes.pdf', '/missing.pdf', '/notes.pdf%00'].each do |url|
    rejects(url) { Materials.validate!(valid.merge('pdf_url' => url), root: root) }
  end
  root.join('page.html').write('<html>not a PDF</html>')
  rejects('local HTML used as a PDF') { Materials.validate!(valid.merge('pdf_url' => '/page.html'), root: root) }
  rejects('missing thumbnail') { Materials.validate!(valid.merge('thumbnail' => '/missing.jpg'), root: root) }
  rejects('incorrect type') { Materials.validate!(valid.merge('kind' => 'Blog post'), root: root) }
  rejects('missing title') { Materials.validate!(valid.merge('title' => ''), root: root) }
  rejects('invalid year') { Materials.validate!(valid.merge('year' => '2026'), root: root) }
end
puts 'PASS: local/external material contracts and unsafe URL rejection'
