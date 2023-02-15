from argparse import ArgumentParser
from PIL import Image

parser = ArgumentParser()
parser.add_argument('image')
args = parser.parse_args()

image = Image.open(args.image)
width, height = image.size
for y in range(height):
    runs = []
    for x in range(width):
        if image.getpixel((x, y)) > (127,):
            color = 'White'
        else:
            color = 'Black'
        if x == 0:
            run_color = color
            run_length = 0
        run_length += 1
        if color != run_color or run_length == width:
            runs.append(f'{run_color} {run_length}')
            run_color = color
            run_length = 0
    print(', '.join(runs))
