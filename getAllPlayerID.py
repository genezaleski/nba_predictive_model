import nba_py
import time

from nba_py.constants import CURRENT_SEASON

from nba_py import player

#test because this module sometimes doesn't work apparently...
#getPlayer1 = player.PlayerList(league_id="00",
#                                      season="2019-20",
#                                      only_current=1)

#print(getPlayer1.info())
#exit()
def getPlayerIDs():
    f = open("allPlayerID.txt","a")    
    for i in range(2020,1947,-1):
        if i > 2000:
            season = str(i-1) + "-" + str(i%1000)
        elif i == 2000:
            season = str(i-1) + "-00"
        else:
            season = str(i-1) + "-" + str((i-900)%1000) 
        print("Getting season " + season + "...")   
        getPlayer = player.PlayerList(league_id="00",
                                      season=season,
                                      only_current=1)
        print("Recieved " + season)
        playerList = getPlayer.info()
        for p in playerList:
            playerID = p['PERSON_ID']
            f.write(str(playerID) + ",")
        time.sleep(5)         
    f.close()
    print("Collected all Player IDs.")

getPlayerIDs()
#print(CURRENT_SEASON)
#playerSummary = player.PlayerSummary(playerID)
#print(playerSummary.headline_stats())





