#! /usr/bin/env ruby

require 'rubygems'
require 'json-schema'

# script takes a pattern of input; for example '/home/json/*.json'
jsfiles = Dir.glob(ARGV[0])
schema = 'csl-data.json'

jsfiles.each do |jsfile|
  begin
    JSON::Validator.validate!(schema, jsfile)
  rescue JSON::Schema::ValidationError
    puts $!.message
  end
end
