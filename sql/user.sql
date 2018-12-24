DROP DATABASE IF EXISTS mybatis;
CREATE DATABASE IF NOT EXISTS mybatis
  CHARACTER SET 'utf8'
  COLLATE 'utf8_general_ci';
USE mybatis;

#用户表
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user (
  id       INT PRIMARY KEY        AUTO_INCREMENT
  COMMENT 'id',

  name     VARCHAR(100) NOT NULL  DEFAULT ''
  COMMENT '用户名',

  password VARCHAR(100) NOT NULL  DEFAULT ''
  COMMENT '密码'
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '用户表';

