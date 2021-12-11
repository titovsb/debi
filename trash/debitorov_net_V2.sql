/*
������ ������� ���������.NET
--------------
������ ������������ ��� ��������������� ����������� ����������� ������������� � ��������� ����������� �������������. ���� ������ ������������ �������� ���������� �� ����������� ��������������, ������������ ������������, ������� ������� �����������. ������������ ��������� ������ ������������� ���������� ������� ������������, ��� ���� �������� ������������ ��� ������������ �������� ���������.
�������� ������� debits. ��� ������� ������� clients ���� ��������� comments ����� ����������� users, ��� ��������� �� ��������.

updated 12/09/2021
- ��������� ���������� � ���������, �������� ����������� �������.

*/


-- ������� 1 2 3 � 5 (ERD � ��������� �����)

DROP DATABASE IF EXISTS debi;
CREATE DATABASE debi;
USE debi;

-- ������������ �������
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    notes VARCHAR(100) DEFAULT '���������� ������ ������������'
);

INSERT INTO users(name) VALUES 
('�����'),('��������'),('��������'), ('���������');


-- ���������� � ������� ������� ����� ���������
DROP TABLE IF EXISTS comments;
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    client_id BIGINT UNSIGNED NOT NULL COMMENT '����� �������',
    user_id BIGINT UNSIGNED NOT NULL,
    msg VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);

INSERT INTO comments(client_id, user_id, msg, created_at) VALUES
(1, 3, '������, ��� � ���� ��������?', '2018-06-06'),
(1, 4, '������������ ���������', '2018-06-07'),
(1, 2, '���� � ������', '2018-06-10'),
(1, 3, '������ � ���� ����� ����?!!!!!!!', '2019-04-04'),
(1, 1, '������ ��� �������������� �� ������� ��� �����!!!', '2019-04-07'),
(1, 3, '������ ����������� �����!!!! ������!!!!', '2019-05-01'),
(1, 1, '��� �������� - �������', '2020-12-12'),
(7, 3, '������������ ��� ����� �� �������', '2021-09-01'),
(8, 3, '������������ ��� ����� �� �������', '2021-09-01');


-- �������
DROP TABLE IF EXISTS clients;
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    user_id BIGINT UNSIGNED DEFAULT 1 COMMENT '������������� ������������',
    flame BIGINT UNSIGNED NULL COMMENT '���������� � �������',
    inn BIGINT UNSIGNED COMMENT '�������� ���� � profiles',
    shortname VARCHAR(50) COMMENT '�������� �������� ��-�� ��� �������� �������������',
    contract_address VARCHAR(255) COMMENT '�������� ����� �� ��������',
    email VARCHAR(100),
    contract_datanum VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE now(),

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (flame) REFERENCES comments(id)
) COMMENT '������ �������������';

INSERT INTO clients(inn, shortname, email, contract_address, contract_datanum) VALUES
(7725808430, '���������, ���', 'info@atmosfera.msk.ru', '������', '�1 �� 01.01.2001'),
(771234567812, '��������� �.�., ��', 'ipgundareva@mail.ru', '������', '�1 �� 02.02.2002'),
(2312345678, '���������� �1, ���', 'pirozhok@gmail.com', '���������', '�1 �� 03.03.2003'),
(5012345678, '�����������, ���', 'sm@sm-group.ru', '���������� �������', '�1 �� 04.04.2004'),
(3312345678, '����������������, ���', 'vop@mail.ru', '��������', '�5 �� 05.05.2005'),
(7711111111, '�����, ���', 'kot123@mail.ru', '������', '�6 �� 06.06.2006'),
(772222222222, '������ �.�, ��', 'dgivanov_ip@mail.ru', '������', '�7 �� 07.07.2007'),
(2333333333, '����������� ����������', 'vostorg@hotmail.com', '���������', '�8 �� 08.08.2008'),
(5044444444, '���� � ������, ���', 'rik@rik.ru', '���������� �������', '�9 �� 09.09.2009'),
(2555555555, '�������������, ��', 'dsp@specsstroi.ru', '�����������', '�10 �� 10.10.2010');


-- ������� ������������ ����������� �� ����������� ������� � ���������
DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    client_id BIGINT UNSIGNED,
    fill_status BIT DEFAULT 0 COMMENT '����� �������� ���������� ������ EGRUL/EGRIP = 1',
    fullname VARCHAR(255),
    region VARCHAR(2) NOT NULL,
    index_egrul VARCHAR(6),
    addres_egrul VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (client_id) REFERENCES clients(id) ON UPDATE CASCADE ON DELETE restrict
    
) COMMENT='�������� � �������������';

INSERT INTO profiles(client_id, fullname, index_egrul, addres_egrul, created_at, updated_at, region) VALUES 
(10,'Synergized solution-oriented instructionset','101010','������ ����� �����������','2010-03-26 03:40:50','1983-09-04 00:22:30', '25'),
(9,'Profit-focused bi-directional product','999999','������ ����� ��','2005-11-15 12:23:36','2000-05-21 00:22:24', '50'),
(8,'Progressive contextually-based hierarchy','888888','������ ����� ���������','2011-03-28 14:29:36','2021-09-07 21:22:57', '23'),
(7,'Persistent national openarchitecture','777777','������ ����� ������','1974-04-08 03:24:56','2021-09-01 11:12:25', '77'),
(6,'Open-source responsive initiative','666666','������ ����� ������','1982-01-22 16:41:44','2021-05-14 09:05:40', '77'),
(5,'Reduced clear-thinking hub','555555','������ ����� ��������','2008-05-13 18:36:21','2021-06-18 23:40:56', '33'),
(4,'Sharable content-based flexibility','444444','������ ����� ��','2021-05-21 20:35:40','2021-01-05 17:32:59', '50'),
(3,'Synchronised client-server instructionset','333333','������ ����� ���������','1981-05-19 05:27:37','2021-09-09 13:01:41', '23'),
(2,'Function-based system-worthy initiative','222222','������ ����� ������','2021-07-11 19:10:56','2021-02-05 22:06:03', '77'),
(1,'Public-key optimizing encryption','111111','������ ����� ������','2012-12-06 02:48:54','2021-06-09 01:05:34', '77');


-- ������ ����������� � ������� ������� ���������
DROP TABLE IF EXISTS post_statuses;
CREATE TABLE post_statuses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO post_statuses VALUES
(1, '����� ����'),
(2, '��������� � ����'),
(3, '���������� � ��������'),
(4, '���������� � �� ��������'),
(5, '����������� ������');


-- ������� � ������������� ��� ������������ ����� ���. �� 
-- ����������� ����� ������ ��� ������� ����������� ������ ����
-- ���� ������� � ����� ���������� ���. �� ����� ����� �� PYTHON
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) COMMENT '��� ����� � �������',
    filename_sig VARCHAR(255) COMMENT '���� ����������� ������� �����������'
);

INSERT INTO posts(filename, filename_sig) VALUES
('1.PDF', '1.sig'),
('2.PDF', '2.sig'),
('3.PDF', '3.sig'),
('4.PDF', '4.sig'),
('5.PDF', '5.sig'),
('6.PDF', '6.sig'),
('7.PDF', '7.sig');

-- ���������� �������� ������� ������
DROP TABLE IF EXISTS debits;
CREATE TABLE debits(
    id SERIAL PRIMARY KEY,
    client_id BIGINT UNSIGNED,
    is_active BIT DEFAULT 0 COMMENT '1 - �������� ����, ����� ���� ������ ����',
    post_id BIGINT UNSIGNED NULL COMMENT '������ �����������',
    debit FLOAT COMMENT 'C���� �������������',
    post_sentdate TIMESTAMP NULL,
    post_tracker BIGINT UNSIGNED NULL COMMENT '������ �� ������ �������� ��������� ������',
    post_delivereddate TIMESTAMP NULL,
    post_status BIGINT UNSIGNED DEFAULT 1 COMMENT '������ �������� �����',
    email_sentdate TIMESTAMP NULL,    
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (client_id) REFERENCES clients(id) ON UPDATE CASCADE ON DELETE restrict,
    FOREIGN KEY (post_status) REFERENCES post_statuses(id),
    FOREIGN KEY (post_id) REFERENCES posts(id),
    
    INDEX idx_user (client_id, debit)
);

INSERT INTO debits(client_id, is_active, post_id, debit, created_at, updated_at) VALUES
(1, 0, 1, 100000.10, '2018-01-01', '2018-01-01'),
(1, 0, 2, 110000.10, '2019-01-01', '2019-01-01'),
(1, 1, 3, 10000.10, '2020-01-01', '2020-01-01'),
(2, 1, 4, 200.20, '2020-02-02', '2020-02-02'),
(3, 1, 5, 3000.30, '2019-03-03', '2019-03-03'),
(7, 1, 6, 70000.70, '2020-07-07', '2019-07-07'),
(10, 1, 7, 101010.10, '2020-07-07', '2019-07-07');

-- ��� ������� 2 � 3 ��������, ��� ���������� ���������� � ������������
UPDATE debits 
SET email_sentdate = '2021-08-08'
WHERE client_id=2 OR client_id=3;


-- ������� 6 ������������ ������� �� ���

## �������� �������������. (join)
SELECT c.shortname, c.inn, d.debit FROM debits d 
JOIN clients c ON d.client_id = c.id 
WHERE is_active = 1;
-- shortname         |inn         |debit   |
-- ------------------+------------+--------+
-- ���������, ���    |  7725808430| 10000.1|
-- ��������� �.�., ��|771234567812|   200.2|
-- ���������� �1, ���|  2312345678|  3000.3|
-- ������ �.�, ��    |772222222222| 70000.7|
-- �������������, �� |  2555555555|101010.0|


## ������������� �� �������� (��������� ������ + join + �����������)
SELECT region, round(sum(debit),2) AS region_deb FROM (
    SELECT p.region, d.debit FROM debits d 
    JOIN profiles p ON d.client_id = p.client_id 
    WHERE is_active = 1) sel
GROUP BY region
ORDER BY region_deb DESC;
-- region|region_deb|
-- ------+----------+
-- 25    |  101010.1|
-- 77    |   80201.0|
-- 23    |    3000.3|


-- ������� 7 �������������

-- ������� �� profiles ��� ������, ������� ����� ����� ��������� � ������� ����� � �� ���� ��������
DROP VIEW IF EXISTS view_expired_profile;
CREATE VIEW view_expired_profile AS
    SELECT * FROM (SELECT id, IF(TIMESTAMPDIFF(DAY, updated_at, NOW()) > 30, 1, 0) AS expired FROM profiles) exp
WHERE expired = 1;

DROP VIEW IF EXISTS view_current_debts;
CREATE VIEW view_current_debts AS 
    SELECT c.shortname, c.inn, d.debit FROM debits d 
        JOIN clients c ON d.client_id = c.id 
WHERE is_active = 1; 

SELECT * FROM view_expired_profile vep ;
SELECT * FROM view_current_debts ORDER BY debit DESC;



-- ������� 8 ���������/�������/��������


## ������������ ��������� ������
DROP PROCEDURE IF EXISTS imperative;
DELIMITER $$
CREATE PROCEDURE imperative()
BEGIN
    DECLARE tmp int;
    SELECT client_id INTO tmp FROM comments GROUP BY client_id ORDER BY count(*) DESC LIMIT 1;
    SELECT u.name, c.msg, 
        CONCAT(TIMESTAMPDIFF(DAY, c.created_at, now()), ' ���� �����') AS far   
    FROM comments c 
    JOIN users u ON c.user_id = u.id 
    WHERE c.client_id = tmp
    ORDER BY c.created_at;
END $$

## ������������� ��������� ������
CREATE PROCEDURE declarative()
BEGIN
    SELECT u.name, c.msg, 
        CONCAT(TIMESTAMPDIFF(DAY, c.created_at, now()), ' ���� �����') AS far
    FROM comments c
    JOIN users u ON c.user_id = u.id
    WHERE
        c.client_id = (
        SELECT client_id
            FROM comments
            GROUP BY client_id
            ORDER BY count(*) DESC
            LIMIT 1)
    ORDER BY c.created_at;
END $$

CREATE FUNCTION get_debt_on_id(id BIGINT UNSIGNED)
RETURNS float DETERMINISTIC 
BEGIN
    RETURN (SELECT debit FROM debits WHERE client_id = id AND is_active = 1);
END $$
DELIMITER ;

CALL imperative();
CALL declarative();
SELECT get_debt_on_id(1) AS `���� ������� 1`;

## ������� �� �������� ������ ����� � ������� debits
## - ���� ����� ���� ����� �������������, �� ������ 45000
## - ���� ������ ����� ���, �� ������ ������ ������. ��� ��������� is_active ������� 0 �� �������.
DROP TRIGGER IF EXISTS new_debit;
DELIMITER $$
CREATE TRIGGER new_debit BEFORE INSERT ON debits
FOR EACH ROW
BEGIN
    IF NEW.debit = (SELECT debit FROM debits WHERE client_id=NEW.client_id AND is_active = 1) THEN 
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='��� ���� ����� ����';
    END IF ;
END $$
DELIMITER ;

-- INSERT INTO debits(client_id, debit) VALUES (1, 10000.1);
-- SELECT * FROM debits WHERE client_id =1;




