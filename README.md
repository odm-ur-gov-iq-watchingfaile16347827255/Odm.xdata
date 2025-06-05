
# 🛡 Aur QR Verification

![cover](A_digital_graphic_displays_a_cover_image_for_a_sof.png)

نظام تحقق رقمي متكامل باستخدام Flask و RSA و QR Code  
يوفر التحقق من صحة الوثائق باستخدام توقيع رقمي وواجهة تحقق مرئية آمنة.

---

## 🚀 الميزات

- ✅ توليد رموز QR موقعة رقميًا
- 🔍 تحقق تلقائي من التوقيع باستخدام مفاتيح RSA
- 📄 عرض ملف PDF رسمي عند نجاح التحقق
- 📥 رفع صورة QR والتحقق منها
- 🧾 توليد تقرير PDF تلقائي يحتوي تفاصيل الوثيقة
- 🌐 متوافق مع Replit, Docker, Heroku, و GitHub Actions
- 🔐 دعم HTTPS عبر Let's Encrypt + NGINX

---

## 🧪 التشغيل المحلي

```bash
pip install -r requirements.txt
python3 verify_app.py
```

---

## 🐳 للتشغيل عبر Docker

```bash
docker-compose up -d --build
```

---

## 🌍 للتشغيل على Replit

1. اربط المشروع من GitHub
2. تأكد أن `.replit` يحتوي:
   ```
   run = "python3 verify_app.py"
   ```

---

## 📄 مثال JSON داخل QR

```json
{
  "msg": "8EKDPLB*adecgh+",
  "sig": "dY72hyrI..."
}
```

---

## 📝 توليد تقرير PDF

عند نجاح التحقق، يتم تلقائيًا تنزيل تقرير باسم `verification_report.pdf`.

---

## 📁 هيكل المشروع

```
.
├── verify_app.py
├── verify_api.py
├── generate_qr.py
├── upload_qr_verify.py
├── report_generator.py
├── static/
│   ├── sample.pdf
│   └── logo.png
├── templates/
│   ├── index.html
│   └── pdf_result.html
├── requirements.txt
├── .replit
├── replit.nix
└── docker-compose.yml
```

---

> تم تطوير هذا النظام لمحاكاة بيئة تحقق رسمية مشابهة لبوابة أور.

