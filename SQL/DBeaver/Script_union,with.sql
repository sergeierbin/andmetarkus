-- 11. ALAMPÄRINGUD - viide teisele päringule:
-- Millised töötajad on keskmiselt andnud allahindlust üle 7,5%?

select salesreptable.name
from salesreptable
where salesreptable.sales_rep_id  in (
	select salestable.sales_rep_id
	from salestable 
	group by sales_rep_id
	having avg(discount ) > 0.075);

-- 12. AJUTISED PÄRINGUTULEMUSED (Common Table Expressions - CTEs): : 
-- Millised töötajad on keskmiselt andnud allahindlust üle 7,5%
-- ja kui suur on keskmine antud allahindlus?

with salesrepdiscount as (
	select s.sales_rep_id , avg(s.discount ) as avg_discount
	from salestable s
	group by s.sales_rep_id 
	having avg(s.discount ) > 0.075)
select salesreptable.name , salesrepdiscount.sales_rep_id, salesrepdiscount.avg_discount
from salesrepdiscount
left join salesreptable
on salesrepdiscount.sales_rep_id = salesreptable.sales_rep_id ;

-- Tegelikud müügid vs eelarve müügiesindaja kaupa.


with sarep_sales as (
	select sales_rep_id, round(sum(quantity*unit_price*(1-discount))::numeric,0) as sales
	from salestable
	group by sales_rep_id)
select salesreptable.name, sarep_sales.sales, budgettable.budget_sum 
from salesreptable
left join sarep_sales
on salesreptable.sales_rep_id = sarep_sales.sales_rep_id
left join budgettable
on salesreptable.sales_rep_id = budgettable.sales_rep_id  ;

-- 13. TABELITE KOMBINEERIMINE
-- 13.1. Leia tabelite pealt unikaalsed väärtused:
-- Leia kliendid, kellel oli müüke 2025. aastal või enne 2021. aastat -- UNION

select customer_id, product_id, sum(quantity)
from salestable
where sale_date >= '2025-01-01'
group by customer_id, product_id
union
select customer_id, product_id, sum(quantity)
from salestable
where sale_date < '2021-12-31'
group by customer_id, product_id;


-- 13.2. Leia kõik väärtused mitmest tabelist:
-- Leia kõik müügid 2025. aastal või enne 2021. aastat -- UNION ALL

select *
from salestable
where sale_date >= '2025-01-01'
union all
select *
from salestable
where sale_date < '2021-12-31';
