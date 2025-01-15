# Footbal and Climate
## Intro
the aim of this project is to combine national team footbal matches history with climate data to explore the impact of weather on matches quality and outcome. from statistical models conducted an impact of weather on the number of goals scored in a match not found. on the other hand the gaps in temperature averages in countries of origin of the two teams playing can play a significant role on the probability of the home team to win. from data overview and analysis, conducted in looker studio, a number of interesting points came up:
1. the majority of goals scored in the second half, more then that there is concentration of scores towards the end of the halfs.
2. some of the top scorers have high rates of goals scored in penalties

## Data
in this project we combine two data sources:
1. national teams footbal matches (link #1)
2. climate data (link #2)

i decided to store and work with the data locally. the final combined data table will be uploaded to gcp to use in looker studio for data analysis and visualization.
the data is connected using the country and city where the match is played. there was gaps in country and city names between the two sources, as such i standardized the footbal data such that it will fit the coutry and city names as they appear in climate data.
due to the fact that the footbal data consists from 3 tables: results (the games outcome), goalscorers (description and names of the scorers), shootouts (penalty outcomes for games ended by penalties) i created dbt models to fast merge or aggragate data and transfer it to gcp when new data is inserted.

## Statistical Models and results
i had 2 research questions:
1. does temperature or other climate parameter like snow or precipitation impact on the number of goals scored in the match. my assumption is that extreme weather will hurt the energy and speed of the game and so less goals will be scored.
2. does playing home against a team that the average temperature at origin country differs substantialy from the average in the country where the teams play will improve the probabilty of the home team to win.

to better grasp the extreme temperature impact and not linear trend across the whole range of temperatures i transformed the continous temperature variable into cetegorical with 3 possible outcomes: 'cold', 'normal' and 'hot'.
to answer the first question i run 7 variations of simple linear regression (ols). in each variation i added different combination of explanatory (independent) variables. up to the point where i added the teams names as controls, explanatory variables, the normal and hot temperatures recieved negative coefficients i.e in cold wheater (less then 10 degrees celciuc) scored more goals per game on average then in normal and hot weather. after adding teams names as controls the weather coefficients became not significant so we can not drew conclusion from it. other climate parameters: snow and precipitation never in no one of the models got significant coefficient so nothing can be said about this variables.
another approach i took to test the weather impact is to access how the feature (temperature) importance in explainig game total goal scored is changing across the temperatures range. i did this using random forest model, the results show that there is no consistent trend the importance is jumping up and down across all levels of temperature.
to answer my second research question i calculated for each team and month the average temperature at their origin country, this will allow us to measure the absolute difference between the temperature in the day of the match and the home team average temperature in matches played in the specific month (tmp_diff_home) and in same method for away team (tmp_diff_away). because we trying to access probabilities of home win the most appropriate model for that is the logistic regression. in the first version the results show that only tmp_diff_home is significant and for each degree celcius of gap the probability of home team to win will deacrease by 1.02%. in the second version i added as explantory variables parameters that indicates on the team strength in the specific year when the game played.  the 4 calculated additional variables:
1. home_goals_ratio - is the ratio between goals scored and goals recieved for home team in specific year
2. away_goals_ratio - is the ratio between goals scored and goals recieved for away team in specific year
3. home_avg_points - is the average points per game, win = 3 point, draw = 1 and loss = 0. a team won all matches in specific year will get home_avg_points = 3
4. away_avg_points - the same as home_avg_points but for the away team
after adding this additional variables as explantory the coefficient of tmp_diff_away turned into non significant. tmp_diff_home stayed significant with even bigger coefficient, -1.74% for each degree celcius. for tmp_diff_away the coeeficient is positive at level of 0.96% for each degree celcius.
for the second research question i also added feature importance test. from the results of this test we learn that the temperature contribute significantly to the explanation power, not far less then the team strength which intuitivly needs to be biggest factor.

## Summary
in this study we tried to test if weather play a role in the quality of footbal matches, measured by the amount of goals scored in a match. and also if weather impact on the probabilty of one of the team playing to win. regrading the first question the impact can be seen but only without improtant explanatory variables like the teams playing. with such results i would conclude that no impact found. regarding the second question, weather shows significant impact on the probabilty of home team to win. this results repeats in both model variations. as final note we can say that climate is not the strongest factor but definitly do play a role and impacts on the outcome of football matches.

## Future Research Directions
my models and methodology were simple and easy to implement. To enrich my research in the future, I could consider the following approaches:
1. **Incorporate More Climate Variables**: Including additional climate parameters such as humidity, wind speed, and air pressure could provide a more comprehensive understanding of weather impacts on football matches.
2. **Advanced Statistical Models**: Utilizing more sophisticated statistical techniques like mixed-effects models or machine learning algorithms could improve the accuracy and robustness of the findings.
3. **Longitudinal Analysis**: Conducting a longitudinal study to observe changes over time and how different climate conditions affect football matches across different periods.
4. **Player-Specific Data**: Integrating player-specific performance data to analyze how individual players are affected by weather conditions.
5. **Geographical Analysis**: Examining regional differences in weather impacts by categorizing matches based on geographical locations and climate zones.
6. **Crowd and Stadium Factors**: Considering the influence of crowd size, stadium type (open or closed), and other environmental factors that might interact with weather conditions.

By exploring these directions, the research can be significantly enriched, providing deeper insights into the relationship between football and climate.

## Links
1. footbal matches - https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017
2. climate data - https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily
this data can be accessed using api: https://www.ncdc.noaa.gov/cdo-web/api/v2/data
3. looker studio workbook - https://lookerstudio.google.com/reporting/4ff1bf90-73f3-4124-87b8-34fa434fbd89

## KeyWords
- Football
- Climate
- Statistical models
- Linear regression
- Logistic regression
- Random forest
- Mixed-effects models
- Data analysis
- Data visualization
- Looker Studio
- GCP
- Environmental factors
- Kaggle
- NOAA    