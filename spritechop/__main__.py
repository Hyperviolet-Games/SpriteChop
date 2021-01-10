from PIL import Image
import json
import os
import sys


def chop(config_path: str, save=True) -> list:
    """Split a sprite sheet based on the configuration file at 
    config_path. Returns list of the names of files created"""
    # TODO optionally set different output folder
    with open(config_path) as f:
        config = json.load(f)
    im = Image.open(config['image_path'])
    w, h = config['width'], config['height']

    path = os.path.split(config['image_path'])

    i = 0
    y = 0
    files = []
    while y < im.height:
        x = 0
        while x < im.width:
            new_img = im.crop((x, y, x+w, y+h))
            if new_img.getchannel("A") != Image.new("RGBA", (w, h)).getchannel("A"):
                if 'names' in config and len(config['names']) > i:
                    name = f'{config["names"][i]}.png'
                else:
                    name = f'{path[1][:-4]}_{i}.png'

                if save:
                    new_img.save(f'{path[0]}/{name}')
                files.append(name)
            i += 1
            x += w
        y += h
    return files


if __name__ == "__main__":
    # TODO Argparse
    if len(sys.argv) < 2:
        print("Pass a config file please")
        exit()
    chop(sys.argv[1])
