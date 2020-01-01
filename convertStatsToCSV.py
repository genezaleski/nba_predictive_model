import ast 
import csv

with open('playerStats.csv','w',newline='') as f:
    fileCopy = open('playerStatsCopy.csv','w',newline='')
    writer = csv.writer(f)
    writer2 = csv.writer(fileCopy)
    writer.writerow(['player','points','rebounds','assists','class'])
    with open("allPlayerStats.txt","r") as statsFile:
        for line in statsFile:
            currentLine = line.split("],[")
            x = 0
            for subLine in currentLine:
                subLine = subLine.replace("[","").replace("u'","'").replace("]","")
                if subLine.endswith(","):
                    subLine = subLine[:-1]
                print(subLine)
                if subLine: #if subline is not empty
                    casted = ast.literal_eval(subLine)
                    print(str(casted['PLAYER_NAME']) +
                        str(casted['PTS'])+"/"+str(casted['REB'])+"/"+str(casted['AST']))
                    points = casted['PTS']
                    if points == None:
                       casted['PTS'] = 0
                       points = 0
                    rebounds = casted['REB']
                    if rebounds == None:
                       casted['REB'] = 0
                       rebounds=0
                    assists = casted['AST']
                    if assists == None:
                       casted['AST'] = 0
                       assists=0
                    if points > 20 or assists > 10:
                        #class: all star
                        writer.writerow([casted['PLAYER_NAME'],casted['PTS'],casted['REB'],casted['AST'],0])
                        writer2.writerow([casted['PTS'],casted['REB'],casted['AST'],'all_star'])
                    elif rebounds>10:
                        #class: big
                        writer.writerow([casted['PLAYER_NAME'],casted['PTS'],casted['REB'],casted['AST'],2])
                        writer2.writerow([casted['PTS'],casted['REB'],casted['AST'],'big_man'])
                    elif assists>5:
                        #class: distributor
                        writer.writerow([casted['PLAYER_NAME'],casted['PTS'],casted['REB'],casted['AST'],3])
                        writer2.writerow([casted['PTS'],casted['REB'],casted['AST'],'playmaker'])
                    elif points>10:
                        #class: scorer
                        writer.writerow([casted['PLAYER_NAME'],casted['PTS'],casted['REB'],casted['AST'],1])
                        writer2.writerow([casted['PTS'],casted['REB'],casted['AST'],'scorer'])
                    else:
                        #class: normal player
                        writer.writerow([casted['PLAYER_NAME'],casted['PTS'],casted['REB'],casted['AST'],4])
                        writer2.writerow([casted['PTS'],casted['REB'],casted['AST'],'average_player'])
