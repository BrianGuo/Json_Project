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
request2 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists.json?list-name=hardcover-fiction&rank=1&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
books = urlopen(request2)
response2 = books.read()
request3 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/best-sellers/history.json?&age_group=Ages+5+and+up&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
books = urlopen(request3)
response3 = books.read()
request4 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/overview.json?published_date=2013-05-14&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
books = urlopen(request4)
response4 = books.read()
request5 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/names.json?api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
books = urlopen(request5)
response5 = books.read()


#"http://api.nytimes.com/svc/books/v2/lists/hardcover-fiction.json?&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313"

@app.route("/")
@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    #print response
    #print "\n\n"
    #print response2
    #print "\n\n"
    print response3
    print "\n\n"
    #print response4
    #print "\n\n"
    #print response5
    #print "\n\n"
    #app.debug = True
    #app.run()
