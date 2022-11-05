


from flask import  Flask,render_template



app = Flask(__name__)


@app.route("/search")
def search_logo():
    return render_template("search.html")




@app.route("/d")
def a():
    return render_template("d.html")


if __name__ == "__main__":
    app.run()