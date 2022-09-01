CREATE DEFINER=`root`@`localhost` PROCEDURE `detail`()
BEGIN
	select CUST_NAME AS name ,GRADE AS grade
    from customer where OPENING_AMT+RECEIVE_AMT>10000;
END