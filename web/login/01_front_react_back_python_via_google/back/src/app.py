from flask import Flask, request, jsonify
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import jwt
import datetime

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"
JWT_SECRET = "YOUR_SUPER_SECRET_JWT_KEY"

@app.route("/api/auth/google", methods=["POST"])
def google_auth():
    data = request.get_json()
    token = data.get("credential") # The ID Token sent from Next.js frontend

    if not token:
        return jsonify({"error": "Missing token"}), 400

    try:
        # Verify the ID token with Google's public keys
        id_info = id_token.verify_oauth2_token(
            token, 
            google_requests.Request(), 
            GOOGLE_CLIENT_ID
        )

        # Extract user information from payload
        google_id = id_info["sub"]
        email = id_info.get("email")
        name = id_info.get("name")
        picture = id_info.get("picture")

        # --- DATABASE LOGIC HERE ---
        # 1. Look up user by google_id or email in your DB.
        # 2. If user doesn't exist, create a new record.
        # ---------------------------

        # Create your own JWT session token for client authorization
        session_token = jwt.encode(
            {
                "user_id": google_id,
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
            },
            JWT_SECRET,
            algorithm="HS256"
        )

        return jsonify({
            "message": "Authentication successful",
            "token": session_token,
            "user": {
                "email": email,
                "name": name,
                "picture": picture
            }
        }), 200

    except ValueError:
        # Invalid token
        return jsonify({"error": "Invalid Google token"}), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)
