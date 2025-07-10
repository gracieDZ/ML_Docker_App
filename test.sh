curl -X POST http://172.17.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"age": 65, "bmi": 27.5, "blood_pressure": 130}'
