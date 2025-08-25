# Sử dụng Python image chính thức
FROM python:3.10-slim

# Set thư mục làm việc trong container
WORKDIR /app

# Copy file requirements và cài dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Expose port Flask (5000 mặc định)
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]