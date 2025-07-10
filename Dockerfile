# Use official Python image as base
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
COPY model.py .
COPY model.joblib .
COPY index.html .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "model.py"]
