import os
from PIL import Image

directory = 'images'

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename[0] != '.':  # check for hidden files
            with Image.open(os.path.join(root, filename)) as im:
                new_img = im.rotate(90).resize((128, 128)).convert('RGB') # rotate, resize, and reformat for conversion to jpeg
                
                new_filename = os.path.splitext(filename)[0] + '.jpeg' # create new file name
                new_filepath = os.path.join('/opt/icons', new_filename) # append file name to path
                
                new_img.save(new_filepath) # save new image in new_filepath
        else:
            print(root + '/' + filename + ' is not an Image!')
