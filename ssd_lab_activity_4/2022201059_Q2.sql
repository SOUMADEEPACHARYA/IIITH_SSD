CREATE DEFINER=`root`@`localhost` PROCEDURE `C_city`(IN city varchar(35))
BEGIN
	select distinct CUST_NAME from customer where WORKING_AREA=city;
END