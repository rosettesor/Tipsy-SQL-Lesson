"""
model_ar.py
"""

import sqlite3
from datetime import datetime

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * from Users WHERE email=? AND password=?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	if result:
		fields = ["user_id", "email", "password", "name"]
		return dict(zip(fields, result))
	return None

def new_task(db, title, task_user_id):
	c = db.cursor()
	timestamp = datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, "Not Yet Complete", NULL, ?)"""
	result = c.execute(query, (title, timestamp, task_user_id))
	db.commit()
	return result.lastrowid

def get_user(db,user_id):
	c = db.cursor()
	query = """SELECT * from Users WHERE user_id=?"""
	c.execute(query, (user_id,))
	result = c.fetchone()
	if result:
		fields = ["user_id", "email", "password", "name"]
		return dict(zip(fields, result))

def complete_task(db,task_id):
	c = db.cursor()
	timestamp = datetime.now()
	query = """UPDATE Tasks SET completed_at=? WHERE task_id=?"""
	c.execute(query, (timestamp, task_id))
	db.commit()

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE task_id = ?"""
	c.execute(query,  (task_id,))
	result = c.fetchone()
	if result:
		fields = ["task_id", "title", "created_at", "completed_at", "notes", "task_user_id"]
		return dict(zip(fields, result))

def get_tasks(db, task_user_id=None):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE task_user_id = ?"""
	c.execute(query,  (task_user_id,))
	result = c.fetchone()
	if result:
		fields = ["task_id", "title", "created_at", "completed_at", "notes", "task_user_id"]
		return dict(zip(fields, result))
	else: 
		c = db.cursor()
		query = """SELECT * FROM Tasks"""
		c.execute(query,) 
		result = c.fetchall()
		l = []
		for row in result:	
			new_dict = {}
			new_dict['task_id']=row[0]
			new_dict['title']=row[1]
			new_dict['created_at']=row[2]
			new_dict['completed_at']=row[3]
			new_dict['notes']=row[4]
			new_dict['task_user_id']=row[5]
			l.append(new_dict)
		return l

