CREATE TABLE users (id INTEGER primary key autoincrement, email varchar(64), password varchar(64));

CREATE TABLE posts (id INTEGER primary key autoincrement, title varchar(140), body TEXT, user_id INT, created_at TIMESTAMP);

CREATE TABLE votes (id INTEGER primary key autoincrement, user_id INT, post_id INT, value INT);