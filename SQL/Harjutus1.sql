-- 1. VALIMINE
-- 1.1. Valime esimesed 10 rida tabeliga tutvumiseks - LIMIT
SELECT *
FROM SalesTable
LIMIT 10;

SELECT *
FROM SalesRepTable
LIMIT 10;

SELECT *
FROM BudgetSalesRep
LIMIT 10;

-- 1.2. Valime konkreetsed tulbad - tulba nimed eraldada komadega
SELECT
	SaleID,
	Date,
	CustomerID
FROM SalesTable
LIMIT 10;

SELECT
	Budget
FROM BudgetSalesRep
LIMIT 10;

-- 1.3. Valime unikaalsed väärtused - DISTINCT käsk
SELECT DISTINCT ProductID 
FROM SalesTable;

SELECT DISTINCT CustomerID
FROM SalesTable
ORDER BY CustomerID ASC;

-- 2. FILTREERIMINE - kindlate ridade valimine

-- 2.1. FILTREERIMINE - KINDEL VÄÄRTUS: Valime kindla toote müügid - WHERE käsk tekstilise välja puhul
SELECT * 
FROM SalesTable
WHERE ProductID = 'P001';

-- 2.2. FILTREERIMINE - VÄLISTAMINE: Välistame kindla toote müügid - WHERE käsk tekstilise välja puhul

SELECT * 
FROM SalesTable
WHERE ProductID != 'P001';

-- 2.3. FILTREERIMINE - NUMBRLISE VÄÄRTUSE VÕRDLEMINE: Valime ainult müügid, kus kogus on suurem viiest - WHERE käsk numbrilise välja puhul (teised võrdlused: <, <= , >=)

SELECT * 
FROM SalesTable
WHERE Quantity > 5;

-- 2.4. FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid kindlale kliendile - WHERE ning AND

SELECT * 
FROM SalesTable 
WHERE ProductID = 'P001'
AND
Quantity > 5;

-- 2.5. FILTREERIMINE MITME TUNNUSE ALUSEL: Valime kindla toote müügid VÕI kindla kliendi müügid - WHERE ning OR

SELECT * 
FROM SalesTable 
WHERE ProductID = 'P001'
OR
CustomerID = 'C001';

-- 2.6. FILTREERIMINE VAHEMIKU ALUSEL: Valime ainult müügid, kus kogus on 5 ja 8 vahepeal - BETWEEN

SELECT * 
FROM SalesTable 
WHERE Quantity BETWEEN 5 AND 8;

-- 2.7. FILTREERIMINE - VALIME MITU VÄÄRTUST: Valime mitme kindla toote müügid - IN

SELECT * 
FROM SalesTable 
WHERE ProductID IN ('P001', 'P002');

-- 2.8. FILTREERIMINE OSALISE TEKSTI alusel: Valime kõik tooted, mille ID algab 'P00' - LIKE ja %

SELECT *
FROM SalesTable 
WHERE ProductID LIKE 'P00%';

-- 2.9. FILTREERIMINE - TÕSTUTUNDLIKKUSE EEMALDAMINE: Valime kõik tooted, mille ID algab 'P00' või 'p000' - LOWER või UPPER käsk

SELECT * 
FROM SalesTable 
WHERE LOWER(ProductID) = 'P001'; -- Like % , et valida mitu tooded

-- 2.10. FILTREERIMINE - MITME TINGIMUSE KOMBINEERIMINE: Valime müügid, mis esimese toote puhul on kogusega 2 ja teise toote puhul on kogusega 5 - SULGUDE KASUTAMINE

SELECT * 
FROM SalesTable
WHERE (ProductID = 'P001' AND Quantity = 2)
OR (ProductID = 'P002' AND Quantity = 5);


-- 3. SORTEERIMINE: Sorteerime suurema toote hinnaga müügid ette poole - ORDER BY

SELECT * 
FROM SalesTable
ORDER BY UnitPrice DESC
LIMIT 10;

-- 4. ALIAS - TULBALE UUS NIMI VÄLJUNDIS: Date tulbast SalesDate tulp väljundis - AS

SELECT Date AS SalesDate
FROM SalesTable
LIMIT 10;

/*
5. Mitmerealise kommentaari lisamine:
kui tahad mitu rida kommentaari kirjutada, siis alusta / ja * ning lõpeta * ja /
*/

/*
Kommentaar 1
Kommentaar 2
*/

