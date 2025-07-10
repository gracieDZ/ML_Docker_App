# ML Patient Risk Predictor (Dockerized)

This project serves a machine learning model via a Flask API using Docker.

## Run Locally

```bash
sudo docker build -t patient-risk-model .
sudo docker run -p 5000:5000 patient-risk-model

```

## Predict Endpoint
Access the input form page: http://localhost:5000/
POST http://localhost:5000/predict  
Body:
```json
{
  "age": 65,
  "bmi": 27.5,
  "blood_pressure": 130
}
```
