#!/usr/bin/env python3

import os
import re
import csv
import json
from PIL import Image
import datetime as dt
import time
print(time.time())

def cropImage(filename,coords,labl):
    """Crop image specified by filename to coordinates specified."""    
    print(f"DEBUG: cropImage({filename},{coords})")
    
    

    # Open image and get height and width
    im = Image.open(filename)
    w, h = im.width, im.height

    # Work out crop coordinates, top, left, bottom, right
    l = int(coords[0])
    t = int(coords[1])
    r = int(coords[2])
    b = int(coords[3])

    # Crop and save
    im = im.crop((l,t,r,b))
    im.save("output/" + labl+'.jpg')
    
    

# Create output directory if not existing
if not os.path.exists('output'):
    os.makedirs('output')

# Process CSV file - expected format
# heading;heading
# 00000001.jpg?sr.dw=700;{'right': 0.9, 'bottom': 0.8, 'top': 0.1, 'left': 0.2}
# 00000002.jpg?sr.dw=700;{'right': 0.96, 'bottom': 0.86, 'top': 0.2, 'left': 0.25}

with open('train_labels.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for r in csv_reader: 
        r=r[0].split(',')
        try:
            #print(int(r[4]))
            cropImage(r[0],(r[4],r[5],r[6],r[7]),r[3])
        except Exception as e:
            print(e)

