from flask import render_template, Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap

from wikeyword.service import keyword_extractor

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/keyword", methods=["GET", "POST"])
def keyword():
    if request.method == "POST":
        text = request.form["text"]
        word_entities = keyword_extractor.extract(text)
        return render_template(
            "index.html", word_entities=word_entities, input_text=text
        )
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
