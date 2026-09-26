from flask import Flask, request, jsonify
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import jwt
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

app = Flask(__name__)
CORS(
    app,
    origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    supports_credentials=True,
)


# ajuste específico para funcionar no windows, 
# garantindo que o caminho do arquivo .env seja resolvido corretamente
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# ler o arquivo .env
#load_dotenv()


def utc_now():
    """Return the current UTC datetime with timezone information."""
    return datetime.datetime.now(datetime.timezone.utc)


GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
JWT_SECRET = os.getenv("JWT_SECRET")

print("GOOGLE_CLIENT_ID:", GOOGLE_CLIENT_ID)
print("JWT_SECRET loaded:", bool(JWT_SECRET))

if not GOOGLE_CLIENT_ID or not JWT_SECRET:
    raise RuntimeError("GOOGLE_CLIENT_ID and JWT_SECRET must be configured in the backend .env file")



@app.route("/api/auth/google", methods=["POST"])
def google_auth():
    print("Received request for Google authentication")
    data = request.get_json()
    print("Request data:", data)
    token = data.get("credential") # The ID Token sent from Next.js frontend

    if not token:
        return jsonify({"error": "Missing token"}), 400


    # -------------------
    # DEBUG ONLY — do not use this decoded data for authentication
    unverified_payload = jwt.decode(
        token,
        options={"verify_signature": False}
    )

    print("Token audience:", unverified_payload.get("aud"))
    print("Configured client ID:", GOOGLE_CLIENT_ID)
    print("Token issuer:", unverified_payload.get("iss"))
    print("Token email:", unverified_payload.get("email"))

    # ---------------------


    try:
        # Verify the ID token with Google's public keys
        id_info = id_token.verify_oauth2_token(
            token, 
            google_requests.Request(), 
            GOOGLE_CLIENT_ID
        )
        print("Verified ID info:", id_info)

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
                "name": name,
                "picture": picture,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
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

    except ValueError as e:
        print("Google token verification failed:", repr(e))
        return jsonify({
            "error": "Invalid Google token",
            "details": str(e)
        }), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)
