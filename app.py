from flask import Flask, request, render_template,redirect
#http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers
#New York Times Best Selling Books API
import urllib2, json
from urllib2 import urlopen
app = Flask(__name__)
key = "aed470a02daf0898f629d3784516e2d4:11:70183313"
#request = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/names.json?api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#request = urllib2.Request("http://google.com")
#books = urlopen(request)
#response = books.read()
#request2 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists.json?list-name=Combined+Print+And+E-book+Fiction&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#books = urlopen(request2)
#response2 = books.read()
#request3 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/best-sellers/history.json?&author=Gillian+Flynn&title=Gone+Girl&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#books = urlopen(request3)
#response3 = books.read()
#request4 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/overview.json?published_date=2013-05-14&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#books = urlopen(request4)
#response4 = books.read()
#request5 = urllib2.Request("http://api.nytimes.com/svc/books/v2/lists/names.json?api-key=aed470a02daf0898f629d3784516e2d4:11:70183313")
#books = urlopen(request5)
#response5 = books.read()
#booksdict = json.loads(response)


#diction = response.split()

#"http://api.nytimes.com/svc/books/v2/lists/hardcover-fiction.json?&api-key=aed470a02daf0898f629d3784516e2d4:11:70183313"

@app.route("/")
@app.route("/search")
def search():
    return render_template("search.html", methods = ["GET","POST"])

@app.route("/results", methods=['GET','POST'])
def results():
    if request.method == "POST":
        author = request.form['author']
        author = author.replace(" ", "+")
        author = "author="+author+'&'
        title = request.form['book']
        title = title.replace(" ", "+")
        title = "title="+title+'&'
        url = "http://api.nytimes.com/svc/books/v2/lists/best-sellers/history.json?%s%sapi-key=%s" % (author,title,key)
        print url
        request7 = urllib2.Request(url)
        booklist = urlopen(request7)
        response7 = booklist.read()
        booksdict = json.loads(response7)
        webtitle = booksdict['results'][0]['title']
        print webtitle
        webauthor = booksdict['results'][0]['author']
        print webauthor
        webdescription = booksdict['results'][0]['description']
        webprice = booksdict['results'][0]['price']
        return render_template('results.html', title=webtitle,author=webauthor, description=webdescription, price=webprice )
    if request.method == 'GET':
        return render_template('results.html')
        
		


if __name__ == "__main__":
    app.debug = True
    #print json.loads(response3)['results'][0]['author']
    #print "\n\n"
    #print response3
    #print "\n\n"
    #print response4
    #print "\n\n"
    #print response5
    #print "\n\n"
    #app.debug = True
    app.run()

