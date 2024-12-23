-- CREATE TABLE data (
--     id SERIAL PRIMARY KEY,
--     column1 TEXT,
--     column2 NUMERIC,
--     column3 TIMESTAMP
-- );

-- CREATE TABLE weather (
--     id SERIAL PRIMARY KEY,
--     city TEXT NOT NULL,
--     temperature NUMERIC NOT NULL,
--     humidity NUMERIC NOT NULL,
--     timestamp TIMESTAMP NOT NULL
-- );

-- -- database/init.sql
-- CREATE DATABASE etl_db;
-- CREATE TABLE data (
--     id SERIAL PRIMARY KEY,
--     info TEXT
-- );

-- database/init.sql
CREATE DATABASE etl_db;
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city TEXT,
    temperature FLOAT,
    humidity INT,
    timestamp TIMESTAMP
);