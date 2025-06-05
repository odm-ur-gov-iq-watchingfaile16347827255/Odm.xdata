# استخدم صورة Python الرسمية
FROM python:3.11-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى داخل الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# فتح المنفذ المستخدم من قبل Flask
EXPOSE 5000

# تشغيل التطبيق
CMD ["python3", "verify_app.py"]