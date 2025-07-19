from flask import Blueprint, request, jsonify
import db

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/cast', methods=['POST'])
def cast_vote():
    data = request.get_json()
    national_id = data.get('national_id')
    candidate_id = data.get('candidate_id')

    conn = db.get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, has_voted FROM voters WHERE national_id = %s", (national_id,))
    voter = cur.fetchone()
    if not voter:
        return jsonify({'error': 'Voter not found'}), 404
    if voter[1]:
        return jsonify({'error': 'You have already voted'}), 403

    cur.execute("INSERT INTO votes (voter_id, candidate_id) VALUES (%s, %s)", (voter[0], candidate_id))
    cur.execute("UPDATE voters SET has_voted = TRUE WHERE id = %s", (voter[0],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Vote cast successfully'})

@vote_bp.route('/results', methods=['GET'])
def results():
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT candidates.name, COUNT(*) FROM votes JOIN candidates ON votes.candidate_id = candidates.id GROUP BY candidates.name")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({name: count for name, count in rows})