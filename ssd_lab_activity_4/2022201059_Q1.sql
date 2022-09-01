CREATE DEFINER=`root`@`localhost` PROCEDURE `SUMT`(IN num1 INT ,IN num2 INT , OUT num3 INT)
BEGIN
	select (num1+num2) into num3;
END