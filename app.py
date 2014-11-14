from flask import Flask, request, render_template
#http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers
#New York Times Best Selling Books API
import urllib2
app = Flask(__name__)
books = url_open("http://api.nytimes.com/svc/books/v2/hardcover-fiction.json?&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#response = books.read()

if __name__ == "__main__":
    print response
