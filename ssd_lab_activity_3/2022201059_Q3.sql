select distinct Essn ,count(*) as 'Number of projects'
from  DEPARTMENT d join WORKS_ON w on d.Mgr_ssn=w.Essn join PROJECT p on p.Dnum=d.Dnumber
where p.Pname='productY'
group by Essn
