
from flask import Flask, request, render_template_string
import base64, json
from PIL import Image
from io import BytesIO
import os
import qrcode
from pyzbar.pyzbar import decode
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

PUBLIC_KEY_PEM = open("public_key.pem", "rb").read()
public_key = serialization.load_pem_public_key(PUBLIC_KEY_PEM)

HTML_FORM = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>تحقق من صورة QR</title></head>
<body style="text-align:center;">
    <h2>تحقق من توقيع داخل QR</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="qr_image" accept="image/*"><br><br>
        <input type="submit" value="تحقق من الصورة">
    </form>
    {% if result %}
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/upload", methods=["GET", "POST"])
def upload_qr():
    result = None
    if request.method == "POST":
        file = request.files.get("qr_image")
        if file:
            img = Image.open(file.stream)
            decoded = decode(img)
            if decoded:
                try:
                    qr_content = decoded[0].data.decode()
                    data = json.loads(qr_content)
                    msg = data["msg"].encode()
                    sig = base64.b64decode(data["sig"])
                    public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
                    result = "✅ التوقيع صحيح"
                except Exception as e:
                    result = f"❌ التوقيع غير صالح أو QR لا يحتوي على تنسيق مدعوم"
            else:
                result = "❌ لا يمكن قراءة QR من الصورة"
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(port=5060)
