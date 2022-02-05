from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return 'Index Page!'

@app.route('/test')
def health() -> str:
    return 'Test Page'
