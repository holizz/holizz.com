.PHONEY: build download unpack patch diff clean

build: patch

York-alpha8a.tar.gz:
	wget http://www.jwhitham.org.uk/york/York-alpha8a.tar.gz

York-alpha8a.patch.bz2:
	wget http://holizz.com/software/patches/york/York-alpha8a.patch.bz2

pubs.dat:
	wget http://holizz.com/software/patches/york/pubs.dat


unpack: York-alpha8a.tar.gz
	tar xzf $?
# Fix permissions
	chmod -R 755 York-alpha8/

patch: unpack York-alpha8a.patch.bz2 pubs.dat
	bzcat York-alpha8a.patch.bz2 | patch -d York-alpha8/ -p1
	chmod 755 York-alpha8/york
# Additional mods
	mv pubs.dat York-alpha8/

clean:
	rm -rf York-alpha8

diff: unpack
	LC_ALL=C TZ=UTC0 diff -Naur York-alpha8/ York-alpha8.updated/ | bzip2 > York-alpha8a.patch.bz2
