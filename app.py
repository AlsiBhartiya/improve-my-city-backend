from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS
import time # To generate unique IDs

app = Flask(__name__)
CORS(app) # This enables Cross-Origin Resource Sharing

# This is our temporary in-memory "database"
complaints = []

@app.route('/api/complaints', methods=['POST'])
def submit_complaint():
    data = request.get_json()

    # Generate a unique grievance ID based on the current time
    grievance_id = f"G{int(time.time())}"

    new_complaint = {
        "grievanceId": grievance_id,
        "userName": data.get('userName'),
        "userPhone": data.get('userPhone'),
        "userEmail": data.get('userEmail'),
        "userAddress": data.get('userAddress'),
        "description": data.get('description'),
        "department": data.get('department'),
        "category": data.get('category'),
        "status": "Pending" # Default status
    }

    complaints.append(new_complaint)
    print("--- New Complaint Received ---")
    print(new_complaint)
    
    return jsonify({
        "message": "Grievance successfully submitted!", 
        "grievanceId": grievance_id
    }), 201

@app.route('/api/complaints/track/<grievance_id>', methods=['GET'])
def track_complaint(grievance_id):
    for complaint in complaints:
        if complaint['grievanceId'] == grievance_id:
            return jsonify(complaint)
    
    return jsonify({"error": "Grievance ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)