# SpriteChop (WIP)
Tool to split up Sprite Sheets / Atlases into individual sprites

## Usage
eventually...

`python spritechop path/to/json/config`

Where json is a configuration file with the following fields:

* `image_path`: path to the spritesheet
* `width`: width of individual sprites (in pixels)
* `height`: height of individual sprites (in pixels)
* `name_prefix`: (optional) string to be prepended to image files
* `names`: (optional) a list of names, one for each saved sprite. Order should be left to right, top to bottom (skipping empty areas). Any names not supplied will default to `{spritesheet_name}_{index}.png` (applied to all sprites if this field is omitted entirely)

SpriteChop will dump your images in the same folder as the given spritesheet image. Any empty areas (areas with no visible pixels) will be ignored.

## TODO
This project is mostly built on a "stuff I need" basis, but future features I'd like to add include...

* Custom output location
* Non-uniform sprite definitions (i.e. not all sprites in the sheet need
to be the same size)
* More robust naming (so you can skip a name if necessary)
* Alternative output formats (bmp, etc)
* A really fancy GUI