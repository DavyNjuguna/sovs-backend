
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'SOVS Backend is Running!'

@app.route('/healthz')
def health():
    return 'OK'

# Add your other routes and logic here...

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
