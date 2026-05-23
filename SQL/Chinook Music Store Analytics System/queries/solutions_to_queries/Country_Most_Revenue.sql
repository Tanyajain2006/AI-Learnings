SELECT
    BillingCountry AS country,
    SUM(Total) AS total_revenue
FROM
    Invoice
GROUP BY
    country
ORDER BY
    total_revenue DESC
LIMIT
    1;