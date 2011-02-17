#!/usr/bin/env ruby

# Copyright (c) 2008, Tom Adams
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

# Generates en-ALL.{aff,dic} from dictionaries found in dict/*.xpi

# The easiest way to use this language is to install a language pack, and
# replace the *.{aff,dic} files with the en-ALL.{aff,dic} files.

# Bugs:
#
# I think there's something wrong with the handling of the AFF file. Certain
# declinations are incorrectly flagged (i.e. 'dictionaries'), and when
# switching away from the ALL language Firefox tends to die.

require 'rubygems'
begin
  require 'runicode'
rescue LoadError
  puts 'Install the klookup gem!'
  exit
end
require 'set'

enc = 'UTF-8'

`mkdir -p work`
Dir['dict/*.xpi'].each {|x| `unzip -d work -o #{x}`}

# dic
`sort work/dictionaries/*.dic | uniq > en-ALL.dic`
dic = []
Dir['work/dictionaries/*.aff'].each{|a|
  from = open(a).read.split("\n").select{|l|l=~/^SET /}[0].match(/^SET (.+)$/)[1]
  d = a.sub(/\.aff$/,'.dic')
  dic << `iconv -f #{from} -t #{enc} '#{d}' | tr -d '\\r'`.split("\n")
}
open('en-ALL.dic','w+') {|o|
  o.write(dic.sort.uniq.join("\n"))
  o.write("\n")
}

# aff
try = Set.new
data = []
Dir['work/dictionaries/*.aff'].each{|a|
  from = open(a).read.split("\n").select{|l|l=~/^SET /}[0].match(/^SET (.+)$/)[1]
  aff = `iconv -f #{from} -t #{enc} '#{a}' | tr -d '\\r'`.split("\n").select{|l|l !~/^#/ and l !~/^$/}
  aff=aff.select{|l|l !~/^SET/}
  aff.select{|l|l=~/^TRY/}[0].match(/^TRY (.+)$/)[1].each_char {|ch|
    try << ch unless ch==' '
  }
  aff=aff.select{|l|l !~/^TRY/}
  data += aff
}
open('en-ALL.aff','w+') {|o|
  o.write("SET #{enc}\n")
  o.write("TRY #{try.sort.join}\n")
  o.write(data.join("\n"))
  o.write("\n")
}
