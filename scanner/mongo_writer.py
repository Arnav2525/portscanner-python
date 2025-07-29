from pymongo import MongoClient

def save_scan_result(ip, open_ports, uri="mongodb://localhost:27017"):
    client = MongoClient(uri)
    db = client["network_scan"]
    collection = db["open_ports"]
    collection.update_one({"ip": ip}, {"$set": {"open_ports": open_ports}}, upsert=True)
    print(f"✅ Stored scan results for {ip}")
