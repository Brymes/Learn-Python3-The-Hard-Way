from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "GET":
        return render_template("temp.html")
    else:
        name = request.form['name']
        greet = request.form['greet']
        image = request.form['image']
        greeting = f"{greet}, {name}, {image}"
        return render_template("index_t.html", greeting=greeting, image=image)

if __name__ == "__main__":
    app.run()