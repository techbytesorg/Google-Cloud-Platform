from google.cloud import language_v1
import six

def analyze_text_features(text_content):
    """
    uses the Cloud Natural Language API.
    """
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    if isinstance(text_content, six.binary_type):
        text_content = text_content.decode("utf-8")

    document = language_v1.Document(
        content=text_content, 
        type_=language_v1.Document.Type.PLAIN_TEXT,
        language="en"
    )

    # --- 1. Entity Sentiment Analysis ---
    # We call analyze_entity_sentiment to get the combined entity and sentiment info
    try:
        entity_response = client.analyze_entity_sentiment(document=document)
    except Exception as e:
        print(f"Error during Entity Sentiment Analysis: {e}")
        entity_response = None
        
    print("--- Entity Sentiment Results ---")
    if entity_response and entity_response.entities:
        for entity in entity_response.entities:
            # Only print entities that have sentiment information
            if entity.sentiment.score or entity.sentiment.magnitude:
                print(f"  > Entity Name: **{entity.name}** (Type: {language_v1.Entity.Type(entity.type_).name})")
                print(f"    - Score: {entity.sentiment.score:.2f} (Range: -1.0 to 1.0)")
                print(f"    - Magnitude: {entity.sentiment.magnitude:.2f} (Strength of emotion)")
                
                # Check sentiment explicitly for clarity
                if entity.sentiment.score > 0.1:
                    sentiment_label = "Positive"
                elif entity.sentiment.score < -0.1:
                    sentiment_label = "Negative"
                else:
                    sentiment_label = "Neutral/Mixed"
                print(f"    - **Sentiment: {sentiment_label}**")
    else:
        print("  No salient entities with expressed sentiment found.")


    # --- 2. Content Classification ---
    # Content classification is a separate API method
    try:
        classification_response = client.classify_text(document=document)
    except Exception as e:
        print(f"Error during Content Classification: {e}")
        classification_response = None
        
    print("\n--- 🏷️ Content Classification Results ---")
    if classification_response and classification_response.categories:
        print("  Top Categories:")
        for category in classification_response.categories:
            print(f"  - **{category.name}** (Confidence: {category.confidence:.2f})")
    else:
        print("  No categories found for this content. (Requires sufficient length/topic coverage)")


# --- Sample Text ---
sample_review = (
    "The hotel staff was amazing, always smiling and helpful. "
    "However, the food was terrible, burnt and cold. "
    "This review should be classified under travel."
)

analyze_text_features(sample_review)