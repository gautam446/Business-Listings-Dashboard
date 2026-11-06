CREATE DATABASE IF NOT EXISTS business_dashboard;
USE business_dashboard;

CREATE TABLE IF NOT EXISTS listing_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    category VARCHAR(120) NOT NULL,
    city VARCHAR(120) NOT NULL,
    address TEXT,
    phone VARCHAR(30),
    source VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
