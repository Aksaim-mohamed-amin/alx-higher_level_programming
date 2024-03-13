-- Displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`)
FROM temperatures GROUP BY `state`
ORDER BY `state`;
