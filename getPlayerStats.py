import nba_py
from nba_py import player
import time

noRepeats = []
with open('allPlayerID.txt','r') as f:
    for line in f:
        curr = line.split(",")
        for i in curr:
            if i not in noRepeats:
                noRepeats.append(i)
        print(noRepeats)

    with open('allPlayerStats22.txt','w') as statFile:
        for num in noRepeats:
            if(not(len(num) > 10)):
                stats = player.PlayerSummary(num)
                print(stats.headline_stats())
                statFile.write(str(stats.headline_stats()) + ",")
                time.sleep(3)
        exit()

