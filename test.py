from clarifai.client import ClarifaiApi
from clarifai.rest import Image as ClImage

from clarifai.rest import ClarifaiApp



CLARIFAI_APP_ID = "Op0XnWmtvgZ_WqZOatQ70-1Mf-mVv-N_aYrXOKWB"
CLARIFAI_APP_SECRET = "uD2NryDBuy_vUFYt4sCwU75oHCGfOVVfK7yEtcD6"

app = ClarifaiApp()

clarifai_api = ClarifaiApi()  # assumes environment variables are set.
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc1.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc2.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc3.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc4.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc5.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc6.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc7.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc8.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc9.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc10.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc11.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc12.png", concepts=['hillary-clinton'])
app.inputs.create_image_from_filename(filename = "hillaryclinton/binvispics/hc13.png", concepts=['hillary-clinton'])


app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook1.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook2.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook3.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook4.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook5.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook6.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook7.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook8.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook9.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook10.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook11.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook12.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook13.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook14.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook15.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook16.png", concepts=['macbook'])
app.inputs.create_image_from_filename(filename = "macbook/binvispics/macbook17.png", concepts=['macbook'])


model = app.models.create('testing', concepts=['hillary-clinton', 'macbook'])
model.train()
