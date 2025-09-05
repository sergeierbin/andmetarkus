-- Kuupäevadega seotud funktsioonid PostgreSQL-is

-- 1.1. Leia müügikogused kuude lõikes -- TO_CHAR funktsionaalsus

select to_char(s.sale_date, 'YYYY-MM' ) as year_month, SUM(quantity)
from salestable s
group by to_char(s.sale_date, 'YYYY-MM' )
order by  to_char(s.sale_date, 'YYYY-MM' ) asc; 

--  1.2. HARJUTAMISEKS: Leia müügikogused aastate lõikes

select to_char(s.sale_date, 'YYYY' ) as year, SUM(quantity)
from salestable s
group by to_char(s.sale_date, 'YYYY' )
order by  to_char(s.sale_date, 'YYYY' ) asc; 

-- 1.3. Kui palju on viimasest müügist möödas?
-- 1.3.1. I võimalus: age funktsioon, annab tekstilise tulemuse

select age(max(s.sale_date )), max(s.sale_date )
from salestable s ;

-- 1.3.2. II võimalus: current_date ja lahutustehe - annab päevade arvu numbrilise väärtusena

select current_date, max(sale_date), current_date-max(sale_date) as age_in_days
from salestable;

-- 1.4. HARJUTAMISEKS: Kui palju aega on esimesest müügist möödas?

select current_date, age(min(sale_date)), min(sale_date), current_date-min(sale_date) as age_in_days
from salestable;

-- 1.5. Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude kaupa?

-- Loome eelarvetabeli kuude kaupa
with b as (select to_char(budget_date, 'YYYY-MM' ) as yearmonth,
SUM(budget_sum) as budget_sum
from budget_monthly_salesrep
group by to_char(budget_date, 'YYYY-MM')),
-- Loome müügitabeli kuude kaupa
s as (select to_char(sale_date, 'YYYY-MM' ) as yearmonth,
SUM(quantity*unit_price*(1-discount)) as sales_sum
from salestable as s
group by to_char(sale_date, 'YYYY-MM'))
-- Ühendame loodud tabelid
select b.yearmonth, budget_sum, sales_sum, sales_sum-budget_sum as dif_from_budget
from b
left join s on b.yearmonth = s.yearmonth
order by b.yearmonth asc;


-- Lisame tulpa sales_sum jaoks
ALTER TABLE salestable
ADD sales_sum numeric
generated always as
(quantity*unit_price*(1-discount)) stored;

select * from salestable limit 10; 

-- 1.6. HARJUTAMISEKS: Kui palju on tegelikud müügid, eelarve ja nende võrdlus kuude ja müügiesindaja kaupa?
-- Loome eelarvetabeli kuude kaupa
with b as (select to_char(budget_date, 'YYYY-MM' ) as yearmonth, sales_rep_id,
SUM(budget_sum) as budget_sum
from budget_monthly_salesrep
group by to_char(budget_date, 'YYYY-MM'), sales_rep_id), 
-- Loome müügitabeli kuude kaupa
s as (select sales_rep_id, to_char(sale_date, 'YYYY-MM' ) as yearmonth, 
SUM(quantity*unit_price*(1-discount)) as sales_sum
from salestable as s
group by to_char(sale_date, 'YYYY-MM'), sales_rep_id)
-- Ühendame loodud tabelid
select b.yearmonth, b.sales_rep_id, s.sales_rep_id, b.budget_sum, s.sales_sum, s.sales_sum-b.budget_sum as dif_from_budget
from b
left join s on b.yearmonth = s.yearmonth and b.sales_rep_id = s.sales_rep_id 
order by b.yearmonth, s.sales_rep_id asc;
