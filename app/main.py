from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('/config/config.cfg')
@app.route("/")
def hello():
    return app.config['MSG']

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
