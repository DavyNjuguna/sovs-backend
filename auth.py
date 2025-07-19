from flask import Blueprint, request, jsonify
import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    national_id = data.get('national_id')

    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT full_name, has_voted FROM voters WHERE national_id = %s", (national_id,))
    voter = cur.fetchone()
    cur.close()
    conn.close()

    if voter:
        return jsonify({'message': f'Welcome {voter[0]}', 'has_voted': voter[1]})
    return jsonify({'error': 'Voter not found'}), 404