
CREATE TABLE products
(
  id            INT          NOT NULL AUTO_INCREMENT,
  product_name  VARCHAR(255) NOT NULL,
  created_at    timestamp    NOT NULL COMMENT 'CURRENT_TIMESTAMP',
  updated_at    timestamp    NOT NULL COMMENT 'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP',
  asin          VARCHAR(255) NOT NULL,
  quantity      INT          NOT NULL,
  buy_cost      INT          NOT NULL,
  selling_price INT          NOT NULL,
  id            INT          NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name  VARCHAR(255) NOT NULL,
  email      VARCHAR(255) NOT NULL,
  password   VARCHAR(255) NOT NULL,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

ALTER TABLE products
  ADD CONSTRAINT FK_user_TO_product
    FOREIGN KEY (id)
    REFERENCES user (id);
