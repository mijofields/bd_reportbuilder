DROP DATABASE IF EXISTS bd_reportBuilder_db;
CREATE DATABASE bd_reportBuilder_db;
USE bd_reportBuilder_db;

CREATE TABLE profile_dimension(
  dtcc_id INTEGER(10) AUTO_INCREMENT NOT NULL,
  filng_freq ENUM('Monthly', 'Quaterly', 'Annual') NOT NULL,
  firm_nm VARCHAR(100) NOT NULL,
  firm_id VARCHAR(8) UNIQUE NOT NULL,
  adr VARCHAR(100) NOT NULL,
  city CHAR(20) NOT NULL,
  st CHAR(2) NOT NULL,
  zip VARCHAR (5) NOT NULL,
  prd_begin DATE NOT NULL,
  prd_end DATE NOT NULL,
  carries_acct BOOLEAN NOT NULL,
  PRIMARY KEY (dtcc_id)
);







INSERT INTO profile_dimension (filng_freq, firm_nm, firm_id, adr, city, st, zip, prd_begin, prd_end, carries_acct) values ('Monthly', 'Test Brokerage #1', '00000', '123 West Street', 'New York', 'NY', '10001', '2018-08-01', '2018-08-31', FALSE);