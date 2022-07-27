from PIL import Image
from autocrop import Cropper

cropper = Cropper(
    width = 150,
    height = 200,
    face_percent = 50
)

# Get a Numpy array of the cropped image
img_url = "test_imgs/test.jpg"
cropped_array = cropper.crop(img_url)

# Save the cropped image with PIL if a face was detected:
if cropped_array != None :
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save('test_imgs/test.png')