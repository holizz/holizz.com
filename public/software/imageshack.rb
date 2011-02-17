#!/usr/bin/env ruby
#
# Copyright (c) 2008 Tom Adams
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

# imageshack.rb:
#   Prints to STDOUT the URLs of all images found belonging to the username
#   given as the first argument.
# EXAMPLE:
#   ./imageshack.rb foobar > foobar.urls && wget -i foobar.urls

%w/rubygems hpricot open-uri/.each{|r|require r}

user = ARGV[0]
if user.nil?
  puts 'Enter username as first argument.'
  exit
end

iD = (Hpricot(open("http://profile.imageshack.us/user/#{user}/"))/'#id')[0]['value']

base_u = 'http://profile.imageshack.us/homepage/mimages.php?ipage=%s&mode=details&id=' + iD
n = 1

while true
  u = base_u % n
  h = Hpricot(open(u))

  t = (h/'.if').collect {|i| i.parent}
  
  break if t.length == 0

  n += t.length

  def a(b,c)
    (b/".#{c}")[0].inner_html
  end

  t.each do |d|
    puts "http://img#{a(d,'is')}.imageshack.us/img#{a(d,'is')}/#{a(d,'ib')}/#{a(d,'if')}"
    STDOUT.flush
  end
end
