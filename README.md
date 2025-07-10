# ML Patient Risk Predictor (Dockerized)

This project serves a machine learning model via a Flask API using Docker.

## Run Locally

```bash
sudo ocker build -t patient-risk-model .
sudo ocker run -p 5000:5000 patient-risk-model

