from google import genai
model_name = "text-embedding-004" # This model is not yet available.
client = genai.Client(
  vertexai=True, project="training-sandbox-470116", location="global",
)
vectors = client.models.embed_content(model=model_name, contents="This is Vertex AI")
print(vectors)