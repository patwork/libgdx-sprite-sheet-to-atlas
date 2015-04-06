# Simple atlas file generator for libGDX
This python script generates **atlas** files for [libGDX](https://github.com/libgdx/libgdx) [TextureAtlas](https://github.com/libgdx/libgdx/wiki/Texture-packer#textureatlas) class. You can use it with existing sprite sheets downloaded from sites like [OpenGameArt.org](http://opengameart.org).

Usage
-----
> python ./libgdx-sprite-sheet-to-atlas.py sprite-sheet-filename sprite-sheet-width-px sprite-sheet-height-px tile-width-px tile-height-px [tile-count-limit]

* *sprite-sheet-filename* - sprite sheet texture filename
* *sprite-sheet-width-px* - width of sprite sheet texture in pixels
* *sprite-sheet-height-px* - height of sprite sheet texture in pixels
* *tile-width-px* - width of single tile/sprite in pixels
* *tile-height-px* - height of single tile/sprite in pixels
* *tile-count-limit* - limit of generated tiles (optional)

Example
-------
> python ./libgdx-sprite-sheet-to-atlas.py mytiles.png 256 128 128 64

Generated mytiles.atlas:
```
mytiles.png
size: 256,128
format: RGBA8888
filter: Linear,Linear
repeat: none
mytiles_00000
  rotate: false
  xy: 0, 0
  size: 128, 64
  orig: 128, 64
  offset: 0, 0
  index: -1
mytiles_00001
  rotate: false
  xy: 128, 0
  size: 128, 64
  orig: 128, 64
  offset: 0, 0
  index: -1
mytiles_00002
  rotate: false
  xy: 0, 64
  size: 128, 64
  orig: 128, 64
  offset: 0, 0
  index: -1
mytiles_00003
  rotate: false
  xy: 128, 64
  size: 128, 64
  orig: 128, 64
  offset: 0, 0
  index: -1
```

Notes
-----
Every tile in sprite sheet must have the same width and height.

Tiles are in horizontal order, without any gaps between.

Script doesn't check if passed arguments have any sense.

