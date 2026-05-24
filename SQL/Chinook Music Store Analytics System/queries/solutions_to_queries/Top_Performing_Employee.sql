SELECT
    e.FirstName AS Employee_First_Name,
    e.LastName AS Employee_Last_Name,
    SUM(i.Total) AS TotalSales
FROM
    Employee e
JOIN
    Customer c
ON
    e.EmployeeId = c.SupportRepId
JOIN
    Invoice i
ON
    i.CustomerId = c.CustomerId
GROUP BY
    e.FirstName, 
    e.LastName
ORDER BY
    TotalSales DESC
LIMIT
    1;