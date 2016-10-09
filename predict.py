from clarifai.client import ClarifaiApi
from clarifai.rest import Image as ClImage

from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
model = app.models.get('testing')
image = ClImage('hillary clinton/bin vis pics/h14.png')
model.predict([image])
