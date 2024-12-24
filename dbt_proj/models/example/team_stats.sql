with part1 as (
    select 
        strftime('%Y', date_ts) AS year, 
        home_team as team,
        count(*) as matches,
        sum(home_score) as goals,
        sum(case when home_score > away_score then 1 else 0 end) as win,
        sum(case when home_score = away_score then 1 else 0 end) as draw,
        sum(case when home_score < away_score then 1 else 0 end) as loss
    from {{ ref('results') }}
    group by 1, 2
),
part2 as (
    select 
        strftime('%Y', date_ts) AS year, 
        away_team as team,
        count(*) as matches,
        sum(away_score) as goals,
        sum(case when home_score < away_score then 1 else 0 end) as win,
        sum(case when home_score = away_score then 1 else 0 end) as draw,
        sum(case when home_score > away_score then 1 else 0 end) as loss
    from {{ ref('results') }}
    group by 1, 2
),
part3 as (
    select * from part1
    union all
    select * from part2
),
part4 as(
    select 
    year, 
    team,
    sum(matches) as matches,
    sum(goals) as goals,
    sum(win) as win,
    sum(draw) as draw,
    sum(loss) as loss,
    cast(sum(win) as double) / cast(sum(matches) as double) as win_prop,
    cast(sum(goals) as double) / cast(sum(matches) as double) as goals_per_match
    from part3
    group by 1, 2
)
select *,
rank() over (partition by year order by win_prop desc) as win_rank,
rank() over (partition by year order by goals_per_match desc) as goals_rank
from part4
where matches > 10
