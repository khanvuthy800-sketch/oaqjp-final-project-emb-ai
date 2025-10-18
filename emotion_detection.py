import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make the POST request to the Watson NLP service
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        # Return error message if request fails
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        # Return error message if JSON parsing fails
        return {"error": f"JSON parsing failed: {str(e)}"}