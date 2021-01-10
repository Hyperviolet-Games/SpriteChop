from PIL import Image
import json
import sys


def chop(config_path: str) -> int:
    """Split a sprite sheet based on the configuration file at 
    config_path. returns # of sprites made"""
    with open(config_path) as f:
        config = json.load(f)
    path = config['image_path']
    im = Image.open(config['image_path'])
    w, h = config['width'], config['height']

    i = 0
    y = 0
    count = 0
    while y < im.height:
        x = 0
        while x < im.width:
            new_img = im.crop((x, y, x+w, y+h))
            if new_img.getchannel("A") != Image.new("RGBA", (w, h)).getchannel("A"):
                new_img.save(f'{path[:-4]}_{i}.png')
                count += 1
            i += 1
            x += w
        y += h
    return count


if __name__ == "__main__":
    # TODO Argparse
    if len(sys.argv) < 2:
        print("Pass a config file please")
        exit()
    chop(sys.argv[1])
