"""
seed.py
"""
import model_ar

db = model_ar.connect_db()
task_user_id = model_ar.new_user(db, "achen@gmail.com", "securepassword", "adelaide")
task = model_ar.new_task(db, "programming", task_user_id)
