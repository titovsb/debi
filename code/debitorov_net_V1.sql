/*
project: ДЕБИТОРОВ.NET
updated 01/09/2021
*/


DROP DATABASE IF EXISTS debi;
CREATE DATABASE debi;
USE debi;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    shortname VARCHAR(50) COMMENT 'Короткое название ЮЛ для удобства идентификации',
    email VARCHAR(100),
    phone BIGINT COMMENT '79991112233',  
    created_to DATETIME DEFAULT CURRENT_TIMESTAMP
) COMMENT 'Список пользователей';

DROP TABLE IF EXISTS debits;
CREATE TABLE debits(
    id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    is_active BIT DEFAULT 0 COMMENT '1 - активный долг, может быть только один'
    filename VARCHAR(255),
    debit FLOAT UNSIGNED COMMENT 'Cумма задолженности',
    post_status BIGINT UNSIGNED NULL COMMENT 'текущий статус в программе из таблицы statuses',
    post_id BIGINT UNSIGNED NULL COMMENT 'Ссылка на статус доставки заказного письма',
    email_date TIMESTAMP NULL,    
    
    created_to DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_to DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE restrict,
);

DROP TABLE IF EXISTS posts;
CREATE TABLE posts


DROP TABLE IF EXISTS profile_egrul;
CREATE TABLE profile_egrul (
    id SERIAL,
    user_id, BIGINT UNSIGNED NOT NULL,
    inn VARCHAR(12) NOT NULL,
    kpp VARCHAR(9) NOT NULL,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    created_to DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_to DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
) COMMENT 'реквизиты из egrul.nalog.ru. все реквизиты существенно важны!!!';

DROP TABLE IF EXISTS statuses;
CREATE TABLE statuslist (
    id SERIAL,
    short VARCHAR(30) NOT NULL,
    extend VARCHAR(100),
) COMMENT 'Возможные статусы уведомлений';

-- сразу их заполним
INSERT TABLE statuslist(short, extend) VALUES
#('new', 'не направлено'),    # решено статус начальный не вводить пока
('sent', 'в пути'),
('delivered' 'доставлено'),
