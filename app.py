from flask import Flask, render_template, request, socket

# App config.
app = Flask(__name__)


@app.route("/")
@app.route("/test")
def index():
    nb = 1
    return render_template('index.html', number=nb, vhost=socket.gethostname())


@app.route("/add")
def index():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
