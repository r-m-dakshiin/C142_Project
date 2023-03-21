from flask import Flask,jsonify, request
import csv
import pandas as pd




all_articles = []


with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


liked_articles = []
not_liked_articles = []
did_not_read = []


app = Flask(__name__)


@app.route("/get-movie")


def get_movie():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })


@app.route("/liked-movie", methods = ["POST"])


def liked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "data" : liked_articles,
        "status" : "success"
    })


@app.route("/not_liked_movie", methods = ["POST"])


def not_liked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]


    
    not_liked_articles.append(movie)
    return jsonify({
        "data" : not_liked_articles,
        "status" : "success"
    })






@app.route("/did_not_read", methods = ["POST"])


def did_not_read():
    movie = all_articles[0]
    all_articles = all_articles[1:]


    
    did_not_read.append(movie)
    return jsonify({
        "data" : did_not_read,
        "status" : "success"
    })


if __name__ == "__main__":
    app.run()



