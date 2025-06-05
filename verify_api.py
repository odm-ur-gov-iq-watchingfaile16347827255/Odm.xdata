
from flask import Flask, request, jsonify
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

# المفتاح العام المستخدم للتحقق (يرجى تحديثه حسب الحالة الفعلية)
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

@app.route("/api/verify", methods=["POST"])
def api_verify():
    try:
        data = request.json
        msg = data["msg"].encode()
        sig = base64.b64decode(data["sig"])
        public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
        return jsonify({"valid": True, "message": "Signature is valid"})
    except (InvalidSignature, KeyError, ValueError):
        return jsonify({"valid": False, "message": "Invalid signature"})

if __name__ == "__main__":
    app.run(port=5050)
