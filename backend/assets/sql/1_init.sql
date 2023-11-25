CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE user_permissions (
    user_id INT,
    permission_id INT,
    is_active INT,
    insert_ts TIMESTAMP
);

CREATE TABLE permissions (
    permission_id SERIAL PRIMARY KEY,
    permission VARCHAR(255)
);

--  = = = = = = = = = APPS

CREATE TABLE apps (
    app_id SERIAL PRIMARY KEY,
    app_name VARCHAR(50),
    app_desc VARCHAR(255)
);

CREATE TABLE user_apps (
    user_id INT,
    app_id INT,
    is_active INT,
    insert_ts TIMESTAMP
);

--  = = = = = = = = = RANKY
CREATE TABLE user_ranking (
    user_id INT,
    ranking_id INT,
    is_active INT,
    insert_ts TIMESTAMP
);

CREATE TABLE user_list_items (
    user_id INT,
    list_item_id INT,
    ranking_id INT,
    score FLOAT,
    is_active INT,
    insert_ts TIMESTAMP,
    update_ts TIMESTAMP
);

CREATE TABLE lists (
    list_id SERIAL PRIMARY KEY,
    list_name VARCHAR(255),
    list_desc VARCHAR(255)
);

CREATE TABLE list_items (
    list_item_id SERIAL PRIMARY KEY,
    list_id INT
);


CREATE TABLE ranking (
    ranking_id SERIAL PRIMARY KEY,
    list_id INT,
    ranking_name VARCHAR(255)
);


