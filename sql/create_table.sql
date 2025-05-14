CREATE TABLE IF NOT EXISTS users (
    id_user VARCHAR(50) PRIMARY KEY,
    name_user VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS taxes (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(id_user),
    purchase FLOAT,
    porcentage INT,
    discount FLOAT,
    plastic_bags INT,
    currency VARCHAR(10),
    tax_value FLOAT
);
