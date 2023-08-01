#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<first>\d*)( |-)?(?<second>\d*)( |-)?(?<third>\d*)/).join
