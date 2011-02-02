#!/usr/bin/env ruby

Dir::glob("*.temp").each { |temp|
	puts "Template: #{temp}"
	file = File.new(temp, 'r')
	template = file.read
	file.close
	tempd = temp.gsub(/\.[^\.]*$/, "")
	Dir::mkdir(tempd) unless FileTest::exist? tempd

	Dir::glob("*.cms").each { |fnamein|
		puts "  CMS file: #{fnamein}"
		fnameout = temp.match(/^(.*?)\./).to_a[1].to_s + "/" + fnamein.gsub(/\.cms$/, ".xhtml")
		puts "  Outfile: #{fnameout}"

		file = File.new(fnamein, 'r')
		title = file.readline
		content = file.read
		file.close

		fout = template.dup
		fout.gsub! /<\$title\$>/, title
		fout.gsub! /<\$content\$>/, content

		File.delete(fnameout) if FileTest.exists?(fnameout)
		File.new(fnameout, File::CREAT).close

		file = File.new(fnameout, File::RDWR)
		file.write(fout)
		file.close
	}
}

