from PIL import Image
from autocrop import Cropper

cropper = Cropper(
    width = 150,
    height = 200,
    face_percent = 50
)

# Get a Numpy array of the cropped image
img_url = ".TEMP\Webcam HP Truevision HD Date 30 Jul 2022 Time 20 29 06 .jpg"
cropped_array = cropper.crop(img_url)

# Save the cropped image with PIL if a face was detected:
if len(cropped_array) != 0 :
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save('.TEMP\Webcam HP Truevision HD Date 30 Jul 2022 Time 20 29 06.jpg')