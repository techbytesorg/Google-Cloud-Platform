import os
from google.cloud import vision

# Set the path to your service account key (if using service account)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/key.json"

client = vision.ImageAnnotatorClient()

# For a Cloud Storage image
# The google.cloud.vision.Image object can directly handle GCS URIs.
image = vision.Image()
image.source.image_uri = "gs://demo_corp/scones.jpg"

response = client.label_detection(image=image)
labels = response.label_annotations

print("Labels:")
for label in labels:
    print(f"{label.description} (score: {label.score:.2f})")
