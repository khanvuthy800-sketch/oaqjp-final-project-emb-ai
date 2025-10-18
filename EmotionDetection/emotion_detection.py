import requests, json
def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip()=="":
        return{'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id":"emotion_aggregated-workflow_lang_en_stock"}
    input_json={"raw_document":{"text":text_to_analyze}}
    try:
        response=requests.post(url,headers=headers,json=input_json)
        if response.status_code==400:
            return{'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
        response.raise_for_status()
        data=response.json()
        emotions=data['emotionPredictions'][0]['emotion']
        emotion_scores={'anger':emotions['anger'],'disgust':emotions['disgust'],'fear':emotions['fear'],'joy':emotions['joy'],'sadness':emotions['sadness']}
        emotion_scores['dominant_emotion']=max(emotion_scores,key=emotion_scores.get)
        return emotion_scores
    except requests.exceptions.RequestException:
        return{'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
    except(KeyError,IndexError,json.JSONDecodeError):
        return{'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
