from flask import Flask, jsonify

from src import settings

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(port=settings.PORT, debug=settings.DEBUG)
