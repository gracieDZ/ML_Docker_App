# ML Patient Risk Predictor (Dockerized)

This project serves a machine learning model via a Flask API using Docker.

## Run Locally

```bash
sudo docker build -t patient-risk-model .
sudo docker run -p 5000:5000 patient-risk-model

