from flask import Flask, request, render_template
#http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers
#New York Times Best Selling Books API
import urllib2
from urllib2 import urlopen
app = Flask(__name__)
request = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/names.json?api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#request = urllib2.Request("http://google.com")
books = urlopen(request)
response = books.read()

if __name__ == "__main__":
    print response
