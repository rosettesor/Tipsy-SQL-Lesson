"""
model_ac.py
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

	else:
		print "NONE"


def new_task(db, title, task_user_id):
	c = db.cursor()
	time_in = datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, NULL, ?)"""
	result = c.execute(query, (title, time_in, task_user_id))
	db.commit()
	return result.lastrowid

def get_user(db, user_id):
	c = db.cursor()
	query = """SELECT * from Users WHERE user_id = ?"""
	c.execute(query, (user_id,))
	result = c.fetchone()
	if result:
		fields = ["user_id", "email", "password", "name"]
		return dict(zip(fields, result))
	else:
		print "NONE"

def complete_task(db, task_id):
	c = db.cursor()
	time_out = datetime.now()
	query = """UPDATE Tasks SET completed_at=? WHERE user_id=?"""
	c.execute(query, (completed_at, task_id))
	db.commit()
	print "Completed at %r." % (time_out)
