from flask import Flask, redirect
import logging

app = Flask(__name__)

@app.route('/')
def redirect_homepage():
    return redirect("https://glenpark.uk", code=301)

@app.route('/<path:path>')
def fallback(path):
	if(path == "work.html"):
		return redirect("https://glenpark.uk/work", code=301)
	if(path == "books.html"):
		return redirect("https://glenpark.uk/books", code=301)
	if(path == "testimonials.html"):
		return redirect("https://glenpark.uk/testimonials", code=301)
	if(path == "contact.html"):
		return redirect("https://glenpark.uk/contact", code=301)
	return redirect("https://glenpark.uk", code=301)