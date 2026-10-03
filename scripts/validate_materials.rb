#!/usr/bin/env ruby
# frozen_string_literal: true
require_relative 'materials'

begin
  paths = Materials::ROOT.join('_materials').glob('*.md')
  paths.each do |path|
    raise ArgumentError, "Invalid filename: #{path.basename}" unless path.basename.to_s.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\.md\z/)
    Materials.validate!(Materials.read(path))
  end
  puts "PASS: #{paths.size} material record(s); required metadata, files, and safe URLs"
rescue ArgumentError, Psych::Exception => error
  warn error.message
  exit 1
end
