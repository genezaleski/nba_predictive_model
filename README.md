# nba_predictive_model
Data Mining Fall 2019

This project classifies an inputted statline of points, rebounds, and assists into categories such as all star, rebounder, playmaker,
scorer, and average nba player. To create this predictive model, I used the nba_py python module to scrape stats.nba.com for the stats of
the ~~3,000 unique players in the history of the nba. I processed this into a csv with player name, points, reb, assists, and would assign
a class to each player based on semi-arbitrary boundaries I thought of by looking at nba.com. These are used to train both Naive Bayes
and KNN classifers. For more, read the project spec file, "Data Mining Final Report.docx"
