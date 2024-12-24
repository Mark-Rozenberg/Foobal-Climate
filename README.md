# Footbal and Climate
## Intro
the aim of this project is to combine national team footbal matches history with climate data to explore the impact of weather matches quality.

## project process
### part 1 - create local sqlite DB to hold the data
### part 2 - downloading raw data and inserting to DB 
    1. football matches from the source: ???
    2. country codes from noaa: ???
    3. city codes from noaa: ???
### part 3 - standartization
    1. country name
    2. city name
    3. add noaa location_id by city and country names
### part 4 - downloading climate data
### part 5 - using dbt to create views for dashboarding
### part 6 - using airflow to export views to gcs
### part 7 - create workbooks and dashboard in Looker 
    1. top 20 scrores all time
    2. goal scored by year + average score in match by year
    3. goals scored by half
    4. distribution of minute goal score
    5. top scoring team (country), in total + average per game
    6. top 20 home vs away winning prop. by country
    7. average score per game by tournament
    