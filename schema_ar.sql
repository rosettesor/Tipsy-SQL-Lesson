create table Users (
	user_id INTEGER PRIMARY KEY, 
	email VARCHAR(32), 
	password VARCHAR(32), 
	name VARCHAR(52)
);

create table Tasks (
	task_id INTEGER PRIMARY KEY, 
	title VARCHAR(32), 
	created_at DATETIME, 
	completed_at DATETIME, 
	notes TEXT(150), 
	task_user_id INTEGER
);
