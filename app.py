from flask import Flask, request, render_template, redirect
import urllib2
from urllib2 import urlopen
cards = urlopen ("https://irythia-hs.p.mashape.com/cards")
response = cards.read()
app = Flask(__name__)


@app.route("/")
def index():
	with app.test_reqeust_context():
		response = request.get("https://irythia-hs.p.mashape.com/cards", headers = {"X-Mashape-Key": "APP"})


if __name__ == "__main__":
	print response