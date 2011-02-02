//--------------------------------------------------------------------------//
//- Meta -------------------------------------------------------------------//
//
// ==UserScript==
// @name            iPac Fixer
// @namespace       http://holizz.com/
// @description     The library interface known as iPac was hand-crafted by crack-smoking primates, apparently.
// @include         http://ipac.*.*/*
// ==/UserScript==
//
// Author: Tom Adams <http://holizz.com/>
// Revision: 2005-06-06
//
//--------------------------------------------------------------------------//
//- License ----------------------------------------------------------------//
//
//  Greasemonkey userscript to fix the library interface iPac
//  Copyright (C) 2005  Tom Adams
//
//  This program is free software; you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation; either version 2 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program; if not, write to the Free Software
//  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
//--------------------------------------------------------------------------//
//- Fixes ------------------------------------------------------------------//
//
// This script fixes the following bugs in iPac:
// * 000: Search field is always auto-focused
// * 001: javascript: links are used
//
//--------------------------------------------------------------------------//
//- Bugs -------------------------------------------------------------------//
//
// * ``Error: href has no properties''
//   Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.8) Gecko/20050517 Firefox/1.0.4 (Debian package 1.0.4-2)
//   Doesn't seem to affect anything though...
//
//--------------------------------------------------------------------------//
//- Program ----------------------------------------------------------------//

(function () {

    /// 000: Stop the search field from being auto-annoyingly focused

    document.getElementsByTagName('body')[0].setAttribute('onload','');

    /// 001: Change javascript: links to plain links that WORK

    var links = document.getElementsByTagName('a');

    for (var i = 0; i < links.length; i++)
    {
	var link = links[i];
	var href = link.getAttribute('href');
	if (href.match(/^javascript:[^']*'([^']*)'/))
	    link.setAttribute('href', decodeURIComponent(RegExp.lastParen));
    }

})();

