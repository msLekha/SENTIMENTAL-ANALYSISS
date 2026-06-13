from textblob import TextBlob
import nltk
import re
import os
from datetime import datetime

nltk.download('punkt')
history = []


def clean_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text


def analyze_sentiment:

    cleaned_text = clean_text(text)

    blob = TextBlob(cleaned_text)

    polarity = blob.sentiment.polarity

    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment, polarity, subjectivity


def save_result(text, sentiment, polarity):

    with open("sentiment_history.txt", "a") as file:

        file.write("\n====================\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write(f"Text: {text}\n")
        file.write(f"Sentiment: {sentiment}\n")
        file.write(f"Polarity Score: {polarity}\n")


def show_history():

    if len(history) == 0:
        print("\nNo history available.")

    else:
        print("\n===== ANALYSIS HISTORY =====")

        for item in history:
            print(item)

            # Main menu function
def main():

    while True:

        print("\n==============================")
        print(" SENTIMENT ANALYSIS SYSTEM ")
        print("==============================")
        print("1. Analyze Sentiment")
        print("2. View History")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":

            text = input("\nEnter your text: ")

            sentiment, polarity, subjectivity = analyze_sentiment(text)

            print("\n===== RESULT =====")
            print("Sentiment:", sentiment)
            print("Polarity Score:", round(polarity, 2))
            print("Subjectivity Score:", round(subjectivity, 2))

            history.append(
                f"Text: {text} | Sentiment: {sentiment}"
            )

            save_result(text, sentiment, polarity)

        elif choice == "2":

            show_history()

        elif choice == "3":

            print("\nThank you for using Sentiment Analysis!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, or 3.")

main()