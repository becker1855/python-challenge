import os
import csv
py_poll = os.path.join("election_data.csv")
with open(py_poll, newline='') as csvfile:
    pollsheet = csv.reader(csvfile,delimiter=',')
    pollheader = next(pollsheet)
    votelist = []
    namelist = []
    voteindex1 = 0 
    winnercount = 0
    for row in pollsheet:
        votelist.append(row[2])
        votecountnum = len(votelist)
    for name in votelist:
        if name not in namelist:
            namelist.append(name)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votecountnum}")
print("-------------------------")
while voteindex1 < len(namelist):
    votechoice =namelist[voteindex1]
    count = 0
    voteindex2 = 0 
    percentwon = 0
    while voteindex2 < len(votelist):
        if votelist[voteindex2] == votechoice:
            count += 1
            percentwon = (count/votecountnum)*100
        voteindex2 += 1
        if count > winnercount:
            winnercount = count
            winner = votechoice    
    print(f"{votechoice}: {format(percentwon,'.2f')}% ({count})") 
    voteindex1 += 1
    if voteindex1 >= len(namelist):
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")