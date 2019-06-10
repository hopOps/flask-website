from flask import Flask, render_template, flash, request

# App config.
app = Flask(__name__)


@app.route("/")
@app.route("/test")
def index():
    nb = 1
    return render_template('index.html', number=nb)


if __name__ == "__main__":
    app.run()