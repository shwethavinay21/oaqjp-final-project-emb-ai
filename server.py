from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotions and score
    score = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'and sadness': sadness_score,
            }       
    score = str(score)
    return "For the given statement, the system response is {}. The dominant emotion is {}.".format(score,dominant_emotion)
    
    # Render the HTML template using render_index_page
    @app.route("/")
    def render_index_page():
        return render_template('index.html')

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)

