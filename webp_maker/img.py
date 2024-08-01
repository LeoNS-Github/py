from PIL import Image
import os
import shutil


new_images = 'new/'
old_images = 'old/'
out_images = 'output/'

image_patterns = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

files = os.listdir(new_images)

for file in files:
  file_data = file.rsplit('.', 1)
  ext = file_data[-1]
  if ext in image_patterns:
    pass
  file_name = file_data[0]
  image = Image.open(new_images+file)
  image = image.convert('RGB')
  image.save(out_images+file_name+".webp", 'webp', optimize=True, quality=10)

  shutil.move(new_images+file, old_images)
  print(f'Image: {file} converted')
  