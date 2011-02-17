# Note: HTK cannot be downloaded without a username/password. Please download
#       HTK-3.4.tar.gz and put it in this directory.

# Contributor: Tom Adams <tom@holizz.com>
pkgname=htk
pkgver=3.4
pkgrel=3
pkgdesc="a portable toolkit for building and manipulating hidden Markov models"
arch=(i686)
url="http://htk.eng.cam.ac.uk/"
license=('Proprietary')
groups=()
depends=()
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
source=("HTK-$pkgver.tar.gz")
noextract=()
md5sums=("35c23b56eb90c82b2101f1fe1428347a") #generate with 'makepkg -g'

build() {
  cd "$srcdir/$pkgname"

  mkdir "$pkgdir/usr"
  ./configure --prefix="$pkgdir/usr"
  make || return 1
  make install
}

# vim:set ts=2 sw=2 et:
