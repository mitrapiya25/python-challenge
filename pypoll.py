import csv
import os
import sys
import getopt
import re
import operator
NumOfFiles = int(sys.argv[1])
Poll=[]

for i in range(1,(NumOfFiles+1)):
    inputfile = "election_data_" + str(i) +".csv"
    print("Input " + inputfile)
    input_path = os.path.join("Homework",inputfile)
    with open(input_path,newline='',encoding="utf8") as csvinpfile:
       first_row = True
       csvreader = csv.reader(csvinpfile,delimiter=',')
       for pollinp in csvreader:
           if first_row:
             first_row = False
             continue   
           else:  
             Poll.append(pollinp)

voterCount =0
CandCount ={}
Poll = sorted(Poll,key=operator.itemgetter(2))
prev_cand=""

for row in Poll:
     if (row[2]):
         voterCount = voterCount+1 
         curr_cand = row[2]
         if curr_cand != prev_cand:
            CandCount[curr_cand] = 1
         else:
            CandCount[curr_cand] = CandCount[curr_cand]+ 1
         prev_cand = row[2]

output_path = os.path.join("Homework","FinalPollresult.txt")
textfile = open(output_path, 'w') 

print("Total Votes " + str(voterCount))
textfile.write("Total Votes " + str(voterCount) + "\n")

for key in CandCount:
    per_win = (CandCount[key]/voterCount)* 100
    print(key +" : " +  str(per_win) +"% " + "(" + str(CandCount[key]) + ")") 
    textfile.write(key +" : " +  str(per_win) +"% " + "(" + str(CandCount[key]) + ")" + "\n") 

winner= max(CandCount, key=CandCount.get)  
print(" Winner is " + winner) 
textfile.write(" Winner is " + winner) 

textfile.close() 
 
