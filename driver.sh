#!/bin/sh

#Get complete list of player IDs for all of NBA history.
python getAllPlayerID.py

#For each player ID, query stats for that ID from stats.nba.com
python getPlayerStats.py

#Convert downloaded stats to CSV, creating training data for classification
python convertStatsToCSV.py

#Run Naive Bayes classifier on data
python naiveBayes.py ./playerStats.csv

#Run KNN Classifier on data
python knnClassifier.py ./playerStats.csv
