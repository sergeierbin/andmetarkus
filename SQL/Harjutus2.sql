-- 6. ARVUTUSED - võimalik teha aritmeetilisi tehteid (+, -, /, *) tulpade loomiseks, filtreerimiseks ja sorteerimiseks
-- 6.1. ARVUTUS - Leia müügisummad, kus müügisumma on suurem kui 500 ja järjesta müügisumma alusel kasvavalt

SELECT
	Round(Quantity*UnitPrice*(1-Discount),2) AS SalesSum
From SalesTable
WHERE SalesSum > 500
ORDER BY SalesSum ASC;    

-- 7. AGREGEERIMINE
SELECT COUNT(SaleID) 
FROM SalesTable;


-- 7.1. LOENDAMINE: Kui palju müügitehinguid on tehtud? - COUNT

-- 7.2. UNIKAALSETE VÄÄRTUSTE LOENDAMINE: Kui palju eri tooteid on müüdud? - COUNT (DISTINCT)

SELECT COUNT(DISTINCT ProductID)
FROM SalesTable;

-- 7.3. SUMMERIMINE: Kui palju on tooteid müüdud? - SUM

SELECT SUM(Quantity)
FROM SalesTable;

-- 7.4. KESKMINE, MIINIMUM, MAKSIMUM: Mis on toodete keskmine, minimaalne ja maksimaalne hind? - AVG, MIN, MAX
SELECT  AVG(UnitPrice), MIN(UnitPrice), Max(UnitPrice)
FROM SalesTable;

-- 7.5. GRUPEERIMINE: Mis on toodete keskmine, minimaalne ja maksimaalne hind toodete kaupa? - GROUP BY
SELECT ProductId, AVG(UnitPrice), MIN(UnitPrice), Max(UnitPrice)
FROM SalesTable
GROUP BY ProductID;

-- 7.6. AGREGEERTITUD VÄÄRTUSE ALUSEL FILTREERIMINE: Näita ainult tooteid, mille keskmine hind on suurem kui 54.50. - HAVING
SELECT ProductID, AVG(UnitPrice) 
FROM SalesTable
GROUP BY ProductID
HAVING AVG(UnitPrice) > 54.5;

-- 8. TÜHI VÄÄRTUS: Näita tooteridu, kus kogus on või ei ole tühi väärtus - IS NULL või IS NOT NULL
SELECT *
FROM SalesTable 
WHERE Quantity IS NULL;

-- 9. VÄÄRTUSE MUUTMINE: Grupeeri tooted kategooriatesse - CASE WHEN
SELECT ProductID,
    CASE 
        WHEN ProductID IN ('P001', 'P002','P003') THEN 'Category 1'
        WHEN ProductID IN ('P004', 'P005') THEN 'Category 2'
        ELSE 'Category 3'
    END AS ProductCategory
FROM SalesTable
GROUP BY ProductID;

-- 10. Concatenate - Ühe tulbana toote ID ja müügiesindaja ID;

SELECT
	CONCAT(ProductID, ' ', SalesRepID)
FROM SalesTable;

-- AGREGEERIMINE HARJUTUSED

-- 1. LOENDAMINE: Kui palju müügiesindajaid on müügiesindaja tabelis?

SELECT COUNT(SalesRepID) 
FROM SalesRepTable;

-- 2. UNIKAALSETE VÄÄRTUSTE LOENDAMINE: Kui palju eri müügiesindajaid on müükide tabelis? 

SELECT COUNT(DISTINCT SalesRepID)
FROM SalesTable;

-- 3. KESKMINE, MIINIMUM, MAKSIMUM: Mis on toodete keskmine, minimaalne ja maksimaalne kogus?

SELECT AVG(Quantity), MIN(Quantity), MAX(Quantity) 
FROM SalesTable;

-- 4. GRUPEERIMINE: Mis on toodete keskmine, minimaalne ja maksimaalne kogus toodete kaupa?

SELECT ProductID, AVG(Quantity), MIN(Quantity), MAX(Quantity) 
FROM SalesTable
GROUP BY ProductID;

-- 5. AGREGEERTITUD VÄÄRTUSE ALUSEL FILTREERIMINE: Näita ainult tooteid, mille keskmine müüdud kogus on suurem kui 5. 

SELECT ProductID, AVG(Quantity) 
FROM SalesTable
GROUP BY ProductID 
HAVING AVG(Quantity) > 5;

-- 6. Grupeeri müügiesindajad tiimidesse.

SELECT *,
    CASE 
        WHEN SalesRepID = 'SR01' THEN 'Tiim1'
        ELSE 'Tiim2'
    END AS Tiim
FROM SalesTable
GROUP BY SalesRepID;

