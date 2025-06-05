
#!/bin/bash

# اسم المجلد
PROJECT_NAME="aur_qr_verification"

# إنشاء مجلد جديد ونسخ الملفات
mkdir -p $PROJECT_NAME/static
mkdir -p $PROJECT_NAME/templates

cp verify_app.py $PROJECT_NAME/
cp verify_api.py $PROJECT_NAME/
cp generate_qr.py $PROJECT_NAME/
cp upload_qr_verify.py $PROJECT_NAME/
cp static/sample.pdf $PROJECT_NAME/static/
cp static/logo.png $PROJECT_NAME/static/
cp templates/index.html $PROJECT_NAME/templates/
cp templates/pdf_result.html $PROJECT_NAME/templates/

# إنشاء README بسيط
cat <<EOL > $PROJECT_NAME/README.md
# Aur Digital Verification - QR Signature System

تحقق رقمي من التوقيعات باستخدام Flask، RSA، و QR Codes.
يشمل:

- توليد QR موقّع رقميًا
- واجهة تحقق رسمية
- API تحقق من التوقيع
- تحميل صورة QR للتحقق التلقائي
- تصميم يحاكي بوابة أور الرسمية

## التشغيل

```bash
pip install flask cryptography qrcode pyzbar pillow
python3 verify_app.py
```

## الدليل

- `/verify_app.py` — واجهة HTML رسمية
- `/verify_api.py` — API تحقق مباشر
- `/generate_qr.py` — توليد QR وتوقيع رقمي
- `/upload_qr_verify.py` — واجهة رفع صورة QR
- `/static/` — يحتوي الشعار والوثيقة
- `/templates/` — صفحات HTML الخاصة بالعرض والتحقق
EOL

echo "✅ المشروع جاهز في مجلد: $PROJECT_NAME"
