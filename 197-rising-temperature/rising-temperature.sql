# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1 INNER JOIN Weather w2 # return the common part we can use any jin here
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature

#WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature
# WE CAN USE WHERE INSTED OF ON HERE 
# DATEDIFF ----> GIVES THE DIFFERENCE BETWEEN TO DATES