# Write your MySQL query statement below
SELECT DISTINCT(author_id) as id
FROM Views
WHERE author_id = viewer_id 
ORDER BY id ASC;

#DISTINCT --> NO DUBLICATIONS
# AS ---> RENAME THE COLUMN
# ORDER BY __COL_NAME_____ ASC/DSC;