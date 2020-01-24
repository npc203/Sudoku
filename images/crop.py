#!/usr/bin/env python3

import os
import re
import csv
import json
from PIL import Image

def cropImage(filename,coords):
    """Crop image specified by filename to coordinates specified."""
    print(f"DEBUG: cropImage({filename},{coords})")

    # Open image and get height and width
    im = Image.open(filename)
    w, h = im.width, im.height

    # Work out crop coordinates, top, left, bottom, right
    l = int(coords['left']  * w)
    r = int(coords['right'] * w)
    t = int(coords['top']   * h)
    b = int(coords['bottom']* h)

    # Crop and save
    im = im.crop((l,t,r,b))
    im.save("output/" + filename)
    return

# Create output directory if not existing
if not os.path.exists('output'):
    os.makedirs('output')

# Process CSV file - expected format
# heading;heading
# 00000001.jpg?sr.dw=700;{'right': 0.9, 'bottom': 0.8, 'top': 0.1, 'left': 0.2}
# 00000002.jpg?sr.dw=700;{'right': 0.96, 'bottom': 0.86, 'top': 0.2, 'left': 0.25}

with open('train_labels.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        fieldA, fieldB = row[:2]

        # Ignore header lines
        if not "jpg" in fieldA:
            continue

        # Strip trailing rubbish off filename
        filename = re.sub("\?.*","",fieldA)
        print(f"DEBUG: filename={filename}")

        # Replace single quotes in JSON with double quotes
        JSON = fieldB.replace("'",'"')
        print(f"DEBUG: JSON={JSON}")
        coords = json.loads(JSON)
        print(f"DEBUG: coords={coords}")

        cropImage(filename, coords)
