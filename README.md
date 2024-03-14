# Creating a machine learning model to predict the outcomes of football matches. 

### Project Overview

My data analysis journey started by learning about data analysis processes and tools. For the last few months, I learned how to use Excel, Python, R and SQL to extract useful insights from large and complex data-sets. 

The next logical step in my journey was to develop my first predictive machine learning algorithm. To do so, I decided to use python programming in order to develop a random - forest classifier. Although I could use a random forest algorithm about virtually anything, I decided to use my passion about football as fuel for this project. 

### Project Layout and Goals

In this project, we will attempt to use factors that govern a football match in order to predict the final outcome of the game. A football match can have 3 possible outcomes, home win, away win and draw. If we try to predict the outcome completely by random, we have a 33% chance to correctly predict the outcome. Given the - 3 possible results - nature of football, we will consider a 33% prediction accuracy as a baseline in order to evaluate our model. 

There are countless factors that govern a football match. We decided to use 20 factors to try and predict the outcome of each game. These factors are the following:

1.  Home team - expected goals per game: The average number of goals per game, that the home team is expected to score, based on the quality of the chances they produce.

2.  Away team - expected goals per game: The average number of goals per game, that the home team is expected to score, based on the quality of the chances they produce.

3.  Home team - expacted goals against: The average number of goals per game, that the home team is expected to concede, based on the quality of the chances their oponent produce.

4.  Away team - expacted goals against: The average number of goals per game, that the home team is expected to concede, based on the quality of the chances their oponent produce.

5.  Home team - clean sheet percentage: The percentage of the matches in which the home team did not concede a goal.

6.  Away team - clean sheet percentage: The percentage of the matches in which the away team did not concede a goal.

7.  Home team - failed to score percentage: The percentage of the matches in which the home team failed to score.

8.  Away team - failed to score percentage: The percentage of the matches in which the away team failed to score.

9.  Home team  - both team to score percentage: The percentage of matches in which both the home team and their opponent managed to score.

10. Away team - both team to score percentage: The percentage of matches in which both the away team and their opponent managed to score.

11. Home team - under 2.5 goals percentage: The percentage of the home teams' matches, in which the total of goals scored was less than 3.

12. Away team - under 2.5 goals percentage: The percentage of the away teams' matches, in which the total of goals scored was less than 3.

13. Home team - over 2.5 goals percentage: The percentage of the home teams' matches, in which the total of goals scored was more than 3.

14. Away team - under 2.5 goals percentage: The percentage of the away teams' matches, in which the total of goals scored was more than 3.

15. Home team - corners for per game: The average number of corners the home team wins per game.

16. Away team - corners for per game: The average number of corners the away team wins per game.

17. Home team - corners against per game: The average number of corners the home team's opponent wins per game.

18. Away team - corners for per game: The average number of corners the away team's opponent wins per game.

19. Home team - cards against per game: The average number of cards against the home team per game.

20. Away team - - cards against per game: The average number of cards against the away team per game.

The ultimate goal of this project is to build a model, that will consider these 20 factors and predict the outcome of the game. Although this model may have some betting applications, the primary goal of this project is not sports betting. We choose to build a model about football for the following reasons. 
- Football is a complicated sport and the results are governed by numerous factors. As a low-scoring sports, sometimes, the results can have a weak connection to the teams' performance.  This complicated nature of football provides an excellent challenge and many learning opportunities.
- The 3 - result nature of football provides a clear baseline (33%), in order to evaluate our model's accuracy
- Football is a personal passion, and that fact provided me with an extra motive for a productive analysis.

### Tools

- Google Sheets
- WPS Sheets
- Python

### Data Sources

The raw data for this project was found in the following websites 

- [FootyStats](https://footystats.org/)

- [The Stats Don't Lie](https://www.thestatsdontlie.com/)

- [Greek Super League](https://www.slgr.gr/el/)

- [Premier League](https://www.premierleague.com/match/93600)

### Data Collection 

In order for the project to be personal and unique, we decided to firstly train my model with data from my native country's football league, the Greek Super League. Firstly, we found the relative data in tables at the FootyStats website. The tables had the following stracture: 

![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/a547ddf1-096d-44f2-a0ea-cc238bb01ea0)

We did not own the paid version of the website and we could not download the tables as csv files. In order to overcome this issue, we created a Google sheet file and entered the data manually. Scrapping the data using python is not authorized by the website's policy.The cards and corner stats were not available at the Footy Stats website, so we sourced these stats from the Stats Don't Lie website.

![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/ea71a985-ffec-4042-918e-7964abf88945)

After gathering all the relevant data, our collective Google Sheet file had the following form:

![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/740fb664-6891-491e-b61d-7071fb09a163)

For our model to work, we needed stats that effectively reflect the teams' performance. All the above stats are averages, so we needed a big enough sample of matches. We took into advantage stats from 24 match days of the 2023/24 Greek Super League. Every team had played 24 competitive games in the season, so the stats above realistically reflect their performance.In addition to the performance stats of each team, we needed to feed our models with the results of each game they played against each other. After all, the main objective of our model is to analyze the performance of the two opposing teams and predict the outcome of the game. We found every result of the 24 first Greek Super League match days and stored them in a Google Sheet file. Except of the game outcome (home win, away win, draw), we also added the number of goals each team scored in each of the games. In the analysis, we will show below, we used the expected goals metric instead of the number of the actual goals scored. As we mentioned before, football is a low scoring goal and the number of goals are not always closely related to the teams' performance. We could say that the expected goals metric is a more fair way to judge a team. The result Google Sheets file is shown below. 

![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/dc6ad963-cf91-47e6-b082-ad284f373619)

We dedicated the following numbers for each game's result:

1 -> Home Win

2 -> Away Win 

3 -> Draw 

In total, we stored data about the result of 159 matches of the 2023/24 Greek Super League
As a final step, we downloaded the stats table and the result table as CSV files with the following names. 

Stats Tabel ->League_Advanced_Stats.csv

Results tabel -> SL_RESULTS.csv

### Data Manipulation 

For our model to work, we needed to contain all the advanced stats and the results we collected, for each of the 159 matches.  We achieved this result using Python and the Pandas Library. 

``` python
# Import the relative libraries
import pandas as pd

# import the raw data-set
league_stats = pd.read_csv("D:\data analysis_2\Case Studies\slpredictions\League_Advanced_Stats.csv")
league_stats = league_stats.dropna(axis=1, how='all')
league_results = pd.read_csv( "D:\data analysis_2\Case Studies\slpredictions\SL_RESULTS.csv")
league_results = league_results.dropna(axis=1, how='all')
league_results = league_results.drop('Unnamed: 7', axis=1)
league_stats = league_stats.set_index('Team')
del league_results['match']
```

Then we used the pandas library to combine the two datasets in one collective table and exported it as a CSV file [sl_final_table.csv]. We did so with the following code: 

```python
# create the collective Dataframe
#home_team
home_team = pd.DataFrame()
home_team['home_team'] = league_results['home_team']
home_team = league_stats.loc[home_team.home_team]
home_team.reset_index(inplace = True, drop = False)
home_team = home_team.add_suffix('_H')

#away_team
away_team = pd.DataFrame()
away_team['away_team'] = league_results['away_team']
away_team = league_stats.loc[away_team.away_team]
away_team.reset_index(inplace = True, drop = False)
away_team = away_team.add_suffix('_A')

#goals and final result 
result = pd.DataFrame()
result['home_goals'] = league_results['home_goals']
result['away_goals'] = league_results['away_goals']
result['result'] = league_results['result']
result

#merge the created tables
df_list = [home_team,away_team,result]
sl_final_table = pd.concat(df_list, axis='columns')

sl_final_table.to_csv("D:\data analysis_2\Case Studies\slpredictions\sl_final_table.csv")
```

The final table had the following stracture: 


![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/5a73149f-f3d8-44eb-8fb0-cddbe37acb0a)



![image](https://github.com/DimitriosLavd/Football_match_predictions/assets/157892523/264d2c43-4d30-4695-a55d-02bfd92b7773)





### Model Building 





















