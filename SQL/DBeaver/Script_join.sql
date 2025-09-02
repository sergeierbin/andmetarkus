-- 10. TABELITE ÜHENDAMINE

-- 10.1. Kõik eelarveread eelarve tabelist ja nendega seotud müügiesindaja nimi müügiesindajate tabelist.

select *
from budgettable b 
left join salesreptable s 
on b.sales_rep_id = s.sales_rep_id ;

-- 10.3. Kõik müügiesindajad müügiesindajate tabelist ja nendega seotud eelarveread eelarve tabelist.

select * 
from salesreptable s 
left join budgettable b 
on s.sales_rep_id = b.sales_rep_id ;

-- 10.4. Näita ainult ridu, millel on müügiesindaja nii eelarve tabelis kui ka väärtus müügiesindajate tabelis.

select *
from salesreptable s 
inner join budgettable b 
on s.sales_rep_id = b.sales_rep_id ;

-- 10.5. Näita kõiki ridu eelarve tabelist ja kõiki ridu müügiesindaja tabelist.

select *
from budgettable b 
full outer join salesreptable s 
on b.sales_rep_id = s.sales_rep_id ;

-- 10.6. Näita ridu eelarve tabelist, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud.

select *
from budgettable b 
left join salesreptable s 
on b.sales_rep_id = s.sales_rep_id 
where s.sales_rep_id is null;

-- 10.7. Näita ridu müügiesindaja tabelist, millele pole kirjeldatud ridu eelarve tabelis.

select *
from salesreptable s 
left join budgettable b 
on s.sales_rep_id = b.sales_rep_id 
where b.sales_rep_id is null;

-- 10.8. Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida.

select *
from salesreptable s 
full outer join budgettable b 
on s.sales_rep_id = b.sales_rep_id 
where s.sales_rep_id is null
or b.sales_rep_id is null;

-- 10.9. Näita ridu müügitabelist, millel on olemas müügiesindaja info eelarve ja müügiesindaja tabelis.

select *
from salestable s  
inner join budgettable b
on s.sales_rep_id = b.sales_rep_id
inner join salesreptable c 
on s.sales_rep_id = c.sales_rep_id ;