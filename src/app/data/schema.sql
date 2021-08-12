DROP TABLE IF EXISTS currency;

CREATE TABLE currency(
    currency_id CHAR(3) PRIMARY KEY,
    currency_name CHAR(15) UNIQUE
)
