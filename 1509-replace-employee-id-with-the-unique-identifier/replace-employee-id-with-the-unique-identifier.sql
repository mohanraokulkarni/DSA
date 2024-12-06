# Write your MySQL query statement below
SELECT eu.unique_id AS unique_id , e.name AS name
FROM Employees e LEFT JOIN EmployeeUNI eu ON e.id = eu.id

# as ---> used to give a table name 
# __Table_1___  LEFT JOIN    ___Table__2___   ON   ____CONDITION____
# left join considers all the rows from the left table, 
#and matchs the value based on condition and if some elements are not present and fill it with a null 
# therefore we have all the names from the table1 and 
#matches with the uniqe_id if table 2 has id same as the names mentioned in table 1 else null value is automatically filled 