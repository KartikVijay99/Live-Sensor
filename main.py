import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


from Sensor.Exception import SensorException
from Sensor.Logger import logging
from Sensor.utils import dump_csv_file_to_mongoDB_collection
import sys
import pymongo



# Secure MongoDB connection
def get_mongo_client():
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://KartikVijay:1234@cluster0.rkivi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",  # Replace with your actual MongoDB URI
            tls=True,  # Use 'tls' instead of 'ssl'
            tlsAllowInvalidCertificates=True,  # Ignore invalid SSL certs
        )
        return client
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == "__main__":
    try:
        file_path = r"C:\Users\hp\Desktop\Sensor Live\aps_failure_training_set1.csv"
        database_name = "APS"
        collection_name = "Sensor"

        # Ensure MongoDB is accessible
        client = get_mongo_client()
        print("✅ Successfully connected to MongoDB!")

        # Dump CSV to MongoDB
        dump_csv_file_to_mongoDB_collection(file_path, database_name, collection_name)

    except Exception as e:
        print(f"❌ Error: {e}")
