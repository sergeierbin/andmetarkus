-- 10. TABELITE ÜHENDAMINE

-- 10.1. Kõik read esimesest tabelist ja seotud read teisest tabelist: Kõik eelarveread, seotud müügiesindajad. - LEFT JOIN

SELECT Budget.SalesRepID, Budget.Budget, SalesRep.Name 
FROM BudgetSalesRep AS  Budget
LEFT JOIN SalesRepTable AS SalesRep 
	ON Budget.SalesRepID = SalesRep.SalesRepID;

-- 10.3. Kõik read teisest tabelist ja seotud read esimesest tabelist: Kõigi müügiesindajate tabelis olevate müügiesindajate eelarveread - RIGHT JOIN

SELECT SalesRep.Name, Budget.Budget
FROM SalesRepTable AS SalesRep
RIGHT JOIN BudgetSalesRep AS Budget
	ON SalesRep.SalesRepID = Budget.SalesRepID; 


-- 10.4. Read, mis on olemas mõlemas tabelis: Näita ainult ridu, millel on müügiesindajal nii eelarve kui ka väärtus müügiesindajate tabelis. - INNER JOIN

SELECT SalesRepTable.Name, BudgetSalesRep.Budget
FROM SalesRepTable 
INNER JOIN BudgetSalesRep 
	ON SalesRepTable.SalesRepID = BudgetSalesRep.SalesRepID;

-- 10.5. Read, mis on olemas ühes või teises tabelis: Näita kõiki eelarveridu ja kõiki müügiesindajate ridu. - FULL OUTER JOIN

SELECT SalesRepTable.Name, BudgetSalesRep.Budget
FROM SalesRepTable 
FULL OUTER JOIN BudgetSalesRep 
	ON SalesRepTable.SalesRepID = BudgetSalesRep.SalesRepID;

-- 10.6. Read, mis on olemas esimeses tabelis ja teises ei ole: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - LEFT JOIN ja IS NULL

SELECT BudgetSalesRep.Budget, SalesRepTable.Name 
FROM BudgetSalesRep
LEFT JOIN SalesRepTable 
	ON SalesRepTable.SalesRepID = BudgetSalesRep.SalesRepID
    WHERE SalesRepTable.SalesRepID IS NULL;

-- 10.7. Read, mida pole esimeses tabelis, aga on teises tabelis: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - RIGHT JOIN ja IS NULL

SELECT BudgetSalesRep.Budget, SalesRepTable.Name 
FROM BudgetSalesRep
RIGHT JOIN SalesRepTable 
	ON BudgetSalesRep.SalesRepID = SalesRepTable.SalesRepID
    WHERE BudgetSalesRep.SalesRepID IS NULL;
    
-- 10.8. Read, mis on puudu ühest või teisest tabelis: Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida. - FULL OUTER JOIN, IS NULL ja OR

SELECT SalesRepTable.Name, BudgetSalesRep.Budget
FROM SalesRepTable
FULL OUTER JOIN BudgetSalesRep
	ON SalesRepTable.SalesRepID = BudgetSalesRep.SalesRepID
    WHERE (SalesRepTable.SalesRepID IS NULL) 
    OR (BudgetSalesRep.SalesRepID IS NULL);


-- 10.9. Rohkem kui kahe tabeli ühendamine: Näita müüke, millel on olemas müügiesindaja eelarve ja müügiesindaja tabelis. - INNER JOIN iga seotava tabeli vahele

SELECT SalesTable.SaleID, SalesRepTable.Name, BudgetSalesRep.Budget 
FROM SalesTable 
INNER JOIN SalesRepTable 
	ON SalesTable.SalesRepID = SalesRepTable.SalesRepID
INNER JOIN BudgetSalesRep  
    ON SalesTable.SalesRepID = BudgetSalesRep.SalesRepID;
