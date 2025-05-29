-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL
);

-- Crear tabla de registros de impuestos
CREATE TABLE IF NOT EXISTS taxes (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR NOT NULL REFERENCES users(id),
    purchase FLOAT NOT NULL,
    porcentage INTEGER NOT NULL,
    discount FLOAT NOT NULL,
    plastic_bags INTEGER NOT NULL,
    currency VARCHAR NOT NULL,
    tax_value FLOAT NOT NULL
);

