from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page/<number>/")
def page(number):
    return render_template('page.html', number=number)

if __name__ == "__main__":
    app.run()
