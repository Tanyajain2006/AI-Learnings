SELECT
    t.TrackId,
    t.name AS track_name,
    t.composer AS track_composer,
    COUNT(*) AS total_purchases
FROM
    InvoiceLine il
JOIN
    Track t
ON
    il.TrackId = t.TrackId
GROUP BY
    t.trackId,
    t.name,
    t.composer
ORDER BY
    total_purchases DESC
LIMIT 
    10;