-- setup mysql server

CREATE DATABASE IF NOT EXISTS ks_dev_db;
CREATE USER 'ks_developers'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'ks_developers'@'localhost';
FLUSH PRIVILEGES;
