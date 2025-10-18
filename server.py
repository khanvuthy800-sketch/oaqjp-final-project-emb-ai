"""
Flask server for Emotion Detection API.
This module provides a web interface for emotion analysis using Watson NLP.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze emotion from text and return formatted response.

    This endpoint accepts text input and returns emotion analysis results
    including anger, disgust, fear, joy, sadness scores and dominant emotion.

    Returns:
        JSON: Emotion analysis results or error message
    """
    try:
        text_to_analyze = request.args.get('textToAnalyze', '')

        # Check for empty input
        if not text_to_analyze.strip():
            return jsonify({
                "error": "Invalid text! Please try again!"
            }), 400

        # Analyze emotion using the emotion_detector package
        result = emotion_detector(text_to_analyze)

        # Check if emotion analysis failed
        if result.get('dominant_emotion') is None:
            return jsonify({
                "error": "Invalid text! Please try again!"
            }), 400

        # Format the response as required
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({
            "response": response_text
        })

    except (ValueError, TypeError, KeyError) as specific_error:
        # Handle specific exceptions instead of general Exception
        print(f"Error processing request: {specific_error}")
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
