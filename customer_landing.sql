CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`customer_landing` (
  `customerName` string,
  `email` string,
  `phone` string,
  `birthDay` string,
  `serialNumber` string,
  `registrationDate` string,
  `lastUpdateDate` string,
  `shareWithResearchAsOfDate` bigint,
  `shareWithPublicAsOfDate` bigint
)