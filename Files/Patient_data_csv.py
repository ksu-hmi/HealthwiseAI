import csv
import random

# Creating a dataset for 30 fictitious patients for the HealthWise demo
patient_data = [] 

for i in range(30):
    patient = {
        "user_id": i + 1,
        "name": f"Patient_{i + 1}",
        "age": random.randint(20, 80),
        "gender": random.choice(["Male", "Female"]),
        "diagnosis": random.choice(["Hypertension", "Diabetes", "Asthma", "Arthritis", "Cancer"]),
        "allergies": random.choice(["None", "Penicillin", "Aspirin", "Codeine"]),
        "medications": random.choice(["Lisinopril", "Insulin", "Albuterol", "Ibuprofen"]),
        "blood_pressure": f"{random.randint(100, 140)}/{random.randint(60, 90)}",
        "heart_rate": random.randint(60, 100),
        "respiratory_rate": random.randint(12, 20),
        "body_temperature": round(random.uniform(97.0, 100.0), 1),
        "insurance_provider": f"Insurance_{i + 1}",
        "policy_number": f"POL{i + 1}23456789",
        "deductible": random.randint(500, 1000),
        "copay": random.randint(40, 100)
    }
    patient_data.append(patient)

# Saving the dataset as a CSV file
fields = list(patient_data[0].keys())
with open('patient_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(patient_data)

print("Dataset saved as patient_data.csv")
