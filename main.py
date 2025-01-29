import os


os.system("python src/data_ingestion.py")
print("Data Ingestion run")

os.system("python src/data_preprocessing.py")
print("Data Preprocessing run")

os.system("python src/feature_engineering.py")
print("Feature Engineering run")

os.system("python src/model_building.py")
print("Model Building run")

os.system("python src/model_evaluation.py")
print("Model Evaluation run")