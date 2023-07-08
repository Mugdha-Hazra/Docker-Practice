# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def display_quotes():
#     # Code to fetch and process the quotes
#     quotes = [...]  # Replace with your code to fetch and process the quotes

#     return render_template("quotes.html", quotes=quotes)
# if __name__ == "__main__":
#     app.run()

import os
from flask import Flask, render_template
from imdb_top_movies import fetch_quotes

app = Flask(__name__)

@app.route("/")
def display_quotes():
    quotes = fetch_quotes()
    template_dir = os.path.abspath("e:/Desktop/python automation")  # Update the path to the directory containing your templates
    app.template_folder = template_dir
    return render_template("quotes.html", quotes=quotes)

if __name__ == "__main__":
    app.run()
