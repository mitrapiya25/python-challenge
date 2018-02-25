import csv
import os
import sys
import operator
print("Give the following arguments")
Filprefix = input("1. File Prefix to process: ")
NumOfFiles = int(input("2. number of files to process"))

Poll=[]
for i in range(1,(NumOfFiles+1)):
    inputfile = Filprefix + str(i) +".csv"
    print("Input " + inputfile)
    input_path = os.path.join("",inputfile)
    with open(input_path,newline='',encoding="utf8") as csvinpfile:
       csvreader = csv.reader(csvinpfile,delimiter=',')
       next(csvreader,None)
       for pollinp in csvreader:
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

output_path = os.path.join("","FinalPollresult.txt")
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
 
