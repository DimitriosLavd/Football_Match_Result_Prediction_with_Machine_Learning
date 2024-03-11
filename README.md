# Creating a machine learning algorithm to predict the outcomes of football matches. 

### Project Overview

My data analysis journey started by learning about data analysis processes and tools. For the last few months, I learned how to use Excel, Python, R and SQL to extract useful insights from large and complex data-sets. 

The next logical step in my journey was to develop my first predictive machine learning algorithm. To do so, I decided to use python programming in order to develop a random - forest classifier. Although I could use a random forest algorithm about virtually anything, I decided to use my passion about football as fuel for this project. 

### Project layout and goals

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

