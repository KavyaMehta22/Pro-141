from flask import Flask, jsonify, request
import csv

all_articles = []

with open ("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data" : all_articles[0],
        "message" : "success"

    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message" : "success"
    })

@app.route("/disliked-articles", methods=["POST"])
def disliked_article():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message" : "success"
    })

if __name__ == "__main__":
    app.run()
