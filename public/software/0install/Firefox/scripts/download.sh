VERSION=2.0.0.6

for LANG in `cat scripts/langs`; do
URL=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/${VERSION}/linux-i686/${LANG}/firefox-${VERSION}.tar.gz &&

mkdir -p ${LANG} &&
wget -nc -P ${LANG} ${URL}

#0publish --add-version=${VERSION} --archive-url=${URL} --set-arch=Linux-i686 --set-stability=stable --set-released=2007-05-30 ${LANG}.xml

done
