#!/usr/bin/env python
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
#

# This script executes itself within the GIMP's batch environment to convert
# all XCF files in the current directory to PNGs.
try:
    gimp # check for the gimp module
    from glob import glob
    files = glob('*.xcf')
    for f in files:
        image = pdb.gimp_file_load(f,f)
        pdb.gimp_image_merge_visible_layers(image, 0) # flatten!
        drawable = pdb.gimp_image_get_active_layer(image)
        newName = f[:-3]+'png'
        pdb.gimp_file_save(image, drawable, newName, newName)
        pdb.gimp_image_delete(image)
    pdb.gimp_quit(1)

# if the module wasn't found, execute this script within the GIMP
except NameError:
    import os, sys
    os.system('gimp --batch-interpreter python-fu-eval -ib - < %s'%sys.argv[0])
