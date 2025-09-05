-- Leia müügisummad toodete kaupa

select product_id, sum(unit_price *quantity *(1-discount ))
from salestable
group by product_id 
order by sum(unit_price *quantity *(1-discount )) desc;

-- Leia müügisummad klientide kaupa

select customer_id , sum(unit_price *quantity *(1-discount ))
from salestable
group by customer_id  
order by sum(unit_price *quantity *(1-discount )) desc;

-- Leia müügisummad müügiesindajate kaupa

select sales_rep_id , sum(unit_price *quantity *(1-discount ))
from salestable
group by sales_rep_id   
order by sum(unit_price *quantity *(1-discount )) desc;

-- Leia müügisummad aastate kaupa

select to_char(sale_date, 'YYYY' ), sum(unit_price *quantity *(1-discount ))
from salestable
group by to_char(sale_date, 'YYYY' )  
order by to_char(sale_date, 'YYYY' ) desc;

-- Lisa müükidele müügisumma kategooriad
-- Large Sale > 500
-- Medium Sale <= 500 and >= 250
-- Small Sale < 250

with a as (SELECT sale_id, sales_sum,
    CASE 
        WHEN sales_sum >500 THEN 'Large Sale'
        WHEN sales_sum between 250 and 500 THEN 'Medium Sale'
        WHEN sales_sum <250 THEN 'Small Sale'
        else 'Other'
    END AS SalesCategory
FROM salestable)
select SalesCategory, count(sale_id), sum(sales_sum)
from a
group by a.SalesCategory 
order by SalesCategory desc;



-- Leia müükide arv ja müügisumma müügisumma kategooriate kaupa
-- Mida veel võiks leida?
