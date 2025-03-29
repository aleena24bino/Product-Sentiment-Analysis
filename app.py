from flask import Flask, render_template, request
import pandas as pd
import os
from sentiment_model import analyze_sentiment, analyze_csv

app = Flask(__name__)
UPLOAD_FOLDER = "dataset"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    review = None

    if request.method == "POST":
        # Check if review text was submitted
        text = request.form.get("review")
        if text:
            sentiment = analyze_sentiment(text)  # Call sentiment analysis function
            review = text  # Store the entered review

        # Check if a CSV file was uploaded
        if "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".csv"):
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(file_path)
                df = analyze_csv(file_path)  # Perform sentiment analysis on CSV

                return render_template("index.html", table=df.to_html())

    return render_template("index.html", sentiment=sentiment, review=review)


if __name__ == "__main__":
    app.run(debug=True)
