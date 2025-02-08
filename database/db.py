from pymongo import MongoClient
from config import DB_URL, DB_NAME

# Inisialisasi Database MongoDB
dbclient = MongoClient(DB_URL)
database = dbclient[DB_NAME]
user_data = database['users']

def add_user(id, user_name):
    """Menambahkan pengguna ke database MongoDB"""
    found = user_data.find_one({'_id': id})
    if not found:
        user_data.insert_one({'_id': id, 'user_name': user_name})

def full_userbase():
    """Mengambil semua ID pengguna dari database MongoDB"""
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

def del_user(user_id: int):
    """Menghapus pengguna dari database MongoDB"""
    user_data.delete_one({'_id': user_id})