select distinct  CONCAT(e1.Fname,' ',e1.Minit,' ',e1.Lname) as 'Full name',
 e1.Ssn as 'ssn' ,e1.Dno as 'Dept. id' ,
 COUNT(*) as 'Number of employees'
from EMPLOYEE e1 join EMPLOYEE e2
on e1.Ssn=e2.Super_ssn
group by e1.Ssn
order by COUNT(*) asc;
