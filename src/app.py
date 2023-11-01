"""Web application that is able to generate memes based on local images and image urls."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from ingestor import Ingestor
from meme_engine import MemeEngine
from quote_engine import QuoteModel
from pathlib import Path

app = Flask(__name__)
meme = MemeEngine("./static")
meme.create_folder()


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []

    for file in quote_files:
        quotes.append(Ingestor.parse(file))

    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)[0]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get("image_url")
    quote = request.form.get("body")
    author = request.form.get("author")
    response = requests.get(image_url)
    if response.status_code == 200:
        dest_path = str(Path("./tmp/", "temp_web_image.jpg"))
        with open(dest_path, "wb") as f:
            f.write(response.content)
        path = meme.make_meme(dest_path, quote, author)
    try:
        os.remove(dest_path)
        print(f"{dest_path} has been deleted.")
    except FileNotFoundError:
        print(f"{dest_path} not found.")
    except Exception as e:
        print(f"An error has occured: {e}")
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
