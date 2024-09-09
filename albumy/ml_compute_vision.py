from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import json

def load_config(creds):
    with open(creds, 'r') as creds_file:
        return json.load(creds_file)

# Load credentials from configuration file
config = load_config('albumy\creds.json')
endpoint = config['endpoint']
key = config['key']

# Initialize the Image Analysis client
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def generate_image_caption(filename):
    # Read the file passed as parameter
    with open(filename, "rb") as f:
        image_data = f.read()

    # Get a caption for the image with a blocking call
    result = client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.CAPTION],
        gender_neutral_caption=True  # Optional, default is False
    )

    # Return the caption if available, else a message indicating no caption
    if result.caption is not None:
        return result.caption.text
    return "No alt available"

def generate_image_tags(filename):
    # Read the file passed as parameter
    with open(filename, "rb") as f:
        image_data = f.read()

    # Get a caption for the image with a blocking call
    result = client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.TAGS, VisualFeatures.OBJECTS]
    )
    # Return tags
    print(result)
    tags = [item['name'] for item in result['tagsResult']['values']] + [item['tags'][0]['name'] for item in result['objectsResult']['values']]
    return list(set(tags))
