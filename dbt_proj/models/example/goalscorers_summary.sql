WITH goalscorers AS (
    SELECT
        scorer,
        team,
        strftime('%Y', date) AS year,
        COUNT(*) AS goals,
        AVG(minute) AS avg_minute,
        SUM(CASE WHEN minute <= 45 THEN 1 ELSE 0 END) AS goals_first_half,
        SUM(CASE WHEN minute > 45 THEN 1 ELSE 0 END) AS goals_second_half,
        SUM(own_goal) AS own_goals,
        SUM(penalty) AS penalties
    FROM
        {{ ref('goalscorers') }}
    WHERE
        scorer IS NOT NULL
    GROUP BY
        1, 2, 3
    ORDER BY
        year DESC
)

SELECT * FROM goalscorers