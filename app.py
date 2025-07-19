from flask import Flask
from flask_cors import CORS
from auth import auth_bp
from vote import vote_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(vote_bp, url_prefix='/vote')

@app.route('/')
def home():
    return {'message': 'SOVS API is running'}

if __name__ == '__main__':
    app.run(debug=True)