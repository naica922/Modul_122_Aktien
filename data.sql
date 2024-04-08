CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS stock_data (
    date DATE,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT
)
