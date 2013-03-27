"""
seed.py
"""
import model_ar

db = model_ar.connect_db()
task_user_id = model_ar.new_user(db, "spongebob@squarepants", "ilovesandy", "SBSQ")
task = model_ar.new_task(db, "look at sunshine", task_user_id)
