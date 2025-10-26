from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# This is our in-memory "database"
complaints = []

# MODIFIED: This function now handles GET and POST
@app.route('/api/complaints', methods=['GET', 'POST'])
def handle_complaints():
    if request.method == 'POST':
        # This is the code for submitting a new complaint
        data = request.get_json()
        grievance_id = f"G{int(time.time())}"

        new_complaint = {
            "grievanceId": grievance_id,
            "userName": data.get('userName'),
            "userPhone": data.get('userPhone'),
            "userEmail": data.get('userEmail'),
            "userAddress": data.get('userAddress'),
            "description": data.get('description'),
            "category": data.get('category'),
            "department": data.get('department'),
            "subCategory": data.get('subCategory'),
            "status": "Pending"
        }

        complaints.append(new_complaint)
        print("--- New Complaint Received ---")
        print(new_complaint)
        
        return jsonify({
            "message": "Grievance successfully submitted!", 
            "grievanceId": grievance_id
        }), 201
    else:
        # NEW: This is the code for getting all complaints
        # This runs by default if the method is GET
        print("--- All Complaints Requested ---")
        return jsonify(complaints)

@app.route('/api/complaints/track/<grievance_id>', methods=['GET'])
def track_complaint(grievance_id):
    for complaint in complaints:
        if complaint['grievanceId'] == grievance_id:
            return jsonify(complaint)
    
    return jsonify({"error": "Grievance ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)