use company;
select distinct CONCAT(Fname,' ',Minit,' ',Lname)as 'Full name', (Mgr_ssn) as 'ssn',
Dnumber as 'Dept. Id',Dname as 'Dept. Name'
from DEPARTMENT d join EMPLOYEE e
ON d.Mgr_Ssn= e.Ssn join WORKS_ON w on e.Ssn=w.Essn
where w.Hours<40