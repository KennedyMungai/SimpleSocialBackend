-- Active: 1670413733633@@127.0.0.1@3306@simple_social_db
-- ------------------------------------------------
-- ------------------------------------------------
-- Creating the posts table
-- ------------------------------------------------
-- ------------------------------------------------
CREATE TABLE posts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    content VARCHAR(255) NOT NULL,
    is_published BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() ON UPDATE NOW()
)