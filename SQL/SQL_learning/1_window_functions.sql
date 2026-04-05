-- TABLE SCHEMA
SELECT * FROM information_schema.tables;

-- COLUMNS WITH DATATYPES
SELECT column_name, data_type from information_schema.columns
WHERE table_name = 'bureau_data';

-- SHOW TABLE DATA
SELECT * FROM bureau_data;

-- SHOW ME TOTAL ACTIVE CREDIT LOAN AMOUNT DEBT PER APPLICATION ID
SELECT sk_id_curr, SUM(amt_credit_sum_debt) AS TOTAL_ACTIVE_CREDIT_LOAN_AMOUNT_DEBT
FROM bureau_data
WHERE credit_active = 'Active'
GROUP BY sk_id_curr
HAVING SUM(amt_credit_sum_debt) > 0
ORDER BY TOTAL_ACTIVE_CREDIT_LOAN_AMOUNT_DEBT DESC
LIMIT 100;

-- TEMP
SELECT 

-- You need to calculate the running total of amt_credit_sum for each client, ordered by the application date (days_credit). 


