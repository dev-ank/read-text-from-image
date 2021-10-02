import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from credentials import api_key


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=api_key
client=vision_v1.ImageAnnotatorClient()


#extracts text from the image using Google Vision API
def text_extraction_from_image(img):

    with open(img,'rb') as image_file:
        content=image_file.read()


    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    texts=response.text_annotations
    para=''
    for text in texts:
        para=text.description
        break

    return para

