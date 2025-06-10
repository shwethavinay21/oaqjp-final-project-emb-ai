from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

"""
"""
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # check if the score is none, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the emotions and score
        return "For the given statement, the system response is {}, {}, {}, {}, {}. The dominant emotion is {}." .format(anger_score,disgust_score,fear_score,joy_score,sadness_score,dominant_emotion)
    
# Render the HTML template using render_index_page
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)

