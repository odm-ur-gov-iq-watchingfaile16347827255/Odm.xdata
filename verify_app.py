
from flask import Flask, request, render_template_string
import base64
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuITYZkZYdW8e86zQdj05
TCgkeqYoIoe2WMkS0Ptdl/eFS/wAUYo5pra42aLx8rnM6dvJQcu+W4AKZNrVzTUh
k0OiCojhmTeMMEVRADhmc09T0Tqicx5HSwKnu/U41FvlsJLLc/EEbgT16VIBP9Fi
84iBO8aCDfJmgsEMd+bfnXmCVeGxf4RNKpnqByv/eu2naz3cAe4JgaMcFocVxZA6
/x2KayK0zKXCj1zFGR4lV414Jpou/HAf9aDt1psu4jJppwR8CsZIHR4qg4rXa57q
6GS4Csj7LCKwjQJ9ShnN0jq58LdO3VZXw+m7AivbEFZQl3oX1U+4LUwNeyQ7P0Kc
/wIDAQAB
-----END PUBLIC KEY-----"""

public_key = serialization.load_pem_public_key(PUBLIC_KEY_PEM.encode())

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>تحقق من التوقيع</title></head>
<body style="text-align:center;">
    <h2>تحقق من التوقيع الرقمي</h2>
    <form method="post">
        <label>ألصق محتوى QR:</label><br>
        <textarea name="qrdata" rows="10" cols="60"></textarea><br><br>
        <input type="submit" value="تحقق">
    </form>
    {% if valid %}
        <p style="color:green;">التوقيع صالح!</p>
        <embed src="/static/sample.pdf" width="80%" height="600px" type="application/pdf">
    {% elif valid == False %}
        <p style="color:red;">التوقيع غير صالح!</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def verify_signature():
    valid = None
    if request.method == "POST":
        try:
            data = json.loads(request.form["qrdata"])
            msg = data["msg"].encode()
            sig = base64.b64decode(data["sig"])
            public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
            valid = True
        except (InvalidSignature, KeyError, ValueError):
            valid = False
    return render_template_string(HTML_FORM, valid=valid)

if __name__ == "__main__":
    app.run(debug=True)
