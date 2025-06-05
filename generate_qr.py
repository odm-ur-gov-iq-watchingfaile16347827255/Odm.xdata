
import base64
import json
import qrcode
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

# إنشاء مفتاح خاص جديد
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# الرسالة المطلوب توقيعها
message = b'8EKDPLB*adecgh+'

# توقيع الرسالة
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# تحويل التوقيع إلى base64
signature_b64 = base64.b64encode(signature).decode()

# تجهيز محتوى QR
qr_payload = {
    "msg": message.decode(),
    "sig": signature_b64
}

# تحويل إلى JSON
qr_data = json.dumps(qr_payload)

# توليد QR Code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("signed_qr.png")

# حفظ المفتاح العام
with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("✅ تم توليد QR وحفظ المفتاح العام في public_key.pem")
