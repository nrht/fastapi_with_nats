DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;


CREATE TABLE roles (
 id SERIAL NOT NULL,
 role VARCHAR,
 PRIMARY KEY (id),
 UNIQUE (role)
);

CREATE TABLE users (
 id SERIAL NOT NULL,
 email VARCHAR,
 name VARCHAR,
 password VARCHAR,
 registered_at TIMESTAMP WITHOUT TIME ZONE,
 role_id INTEGER,
 PRIMARY KEY (id),
 FOREIGN KEY(role_id) REFERENCES roles (id)
);

INSERT INTO roles (id, role) VALUES (DEFAULT, 'administrator');
INSERT INTO roles (id, role) VALUES (DEFAULT, 'director');
INSERT INTO roles (id, role) VALUES (DEFAULT, 'manager');
INSERT INTO roles (id, role) VALUES (DEFAULT, 'member');