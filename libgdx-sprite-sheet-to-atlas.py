#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Simple atlas file generator for libGDX
# https://github.com/patwork/libgdx-sprite-sheet-to-atlas
#

import sys
import os

def createAtlas(args):

	spriteSheetFilename = args[1]
	spriteSheetWidth = int(args[2])
	spriteSheetHeight = int(args[3])
	tileWidth = int(args[4])
	tileHeight = int(args[5])
	tileCountLimit = 0 if len(args) < 7 else int(args[6])

	tmp = os.path.splitext(spriteSheetFilename)[0]
	spriteName = os.path.basename(tmp)
	atlasFilename = tmp + ".atlas"
	count = 0

	with open(atlasFilename, "w") as f:
		f.write("%s\nsize: %d,%d\nformat: RGBA8888\nfilter: Linear,Linear\nrepeat: none\n"
			% (spriteSheetFilename, spriteSheetWidth, spriteSheetHeight))

		for row in range(0, spriteSheetHeight / tileHeight):
			for col in range(0, spriteSheetWidth / tileWidth):
				f.write("%s_%0.5d\n  rotate: false\n  xy: %d, %d\n  size: %d, %d\n  orig: %d, %d\n  offset: 0, 0\n  index: -1\n"
					% (spriteName, count, col * tileWidth, row * tileHeight, tileWidth, tileHeight, tileWidth, tileHeight))
				count = count + 1
				if count == tileCountLimit:
					return

if __name__ == '__main__':

	if len(sys.argv) < 6:
		sys.stderr.write("%s sprite-sheet-filename sprite-sheet-width-px sprite-sheet-height-px tile-width-px tile-height-px [tile-count-limit]\n" % __file__)
		sys.exit(1)

	try:
		createAtlas(sys.argv)
	except IOError as e:
		sys.stderr.write("I/O error(%s): %s\n" % (e.errno, e.strerror))
		sys.exit(2)
	except:
		sys.stderr.write("Error: %s\n" % sys.exc_info()[0])
		sys.exit(3)

	sys.exit(0)

# EoF
# vim: noexpandtab tabstop=4 softtabstop=4 shiftwidth=4
