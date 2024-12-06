# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
GROUP BY v.customer_id

#step1 : creating a join table where we have for each visit there is transaction
# is made or not ----> if no tansaction then the null value is filled automatically
#step2:applying a condinton to select that visited but not transcation using where
#step 3: selecting customer_id and new column with there count  and giving name using as 
#| customer_id | count_no_trans |
#| ----------- | -------------- |
#| 30          | 4              |
# group by is used to sub dividing for each group
#| customer_id | count_no_trans |
#| ----------- | -------------- |
#| 30          | 1              |
#| 96          | 1              |
#| 54          | 2              |