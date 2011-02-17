VERSION=2.0.0.6
DATE=2007-07-27

for LANG in `cat scripts/langs`; do
URL=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/${VERSION}/linux-i686/${LANG}/firefox-${VERSION}.tar.gz &&

#cp template.xml ${LANG}.xml &&
cp ${LANG}/firefox-${VERSION}.tar.gz . &&

0publish --add-version=${VERSION} --archive-url=${URL} --set-arch=Linux-i686 --set-stability=stable --set-released=${DATE} ${LANG}.xml

#sed "s/template/${LANG}/" -i ${LANG}.xml
#grep -v 0.0.0.0 ${LANG}.xml > ${LANG}.xml-temp
#mv -f ${LANG}.xml-temp ${LANG}.xml

done
