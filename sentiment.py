import requests
import json

def query(payload, model_id, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def perform_sentiment_analysis(text):

    # Replace with the sentiment analysis model ID ------------------------------------

    # model_id = "distilbert-base-uncased-finetuned-sst-2-english"  # Positive/Negative

    model_id = "tae898/emoberta-large"  # Joy/Surprise/Neutral/Fear/Disgust/Sadness/Anger



    # API Token Security
    with open('api_tokens.json') as f:
        data = json.load(f)
    
    api_token = data["SENTIMENT_API_TOKEN"]




    payload = {"inputs": text}
    response = query(payload, model_id, api_token)

    if isinstance(response, list) and len(response) > 0:
        sentiments = response[0]  # Extract sentiments from the response

        highest_score = 0.0
        predicted_sentiment = None

        for sentiment in sentiments:
            label = sentiment['label']
            score = sentiment['score']

            # For two sentiments
            # if score > highest_score:
            #     highest_score = score
            #     predicted_sentiment = label

            # For more sentiments
            max_sentiment = max(sentiments, key=lambda x: x['score'])
            predicted_sentiment = max_sentiment['label']
            highest_score = max_sentiment['score']

        return predicted_sentiment if predicted_sentiment else "neutral"
    else:
        return "Error: Sentiment analysis failed."


# Example usage:

# input_text = "ewwwww"
# temp = perform_sentiment_analysis(input_text)
# result = temp.lower()
# print(result)