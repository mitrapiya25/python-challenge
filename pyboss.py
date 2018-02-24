import csv
import os
import sys
import operator
import datetime
NumOfFiles = int(sys.argv[1])
Boss=[]
changedBoss=[]
us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA',
'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA',
'Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS',
'Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI',
'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC',
'North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI',
'South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT',
'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
output_path = os.path.join("Homework","Output.csv")
with open(output_path,"w",newline="",encoding="utf8") as csvopfile:
  csvwriter = csv.writer(csvopfile, delimiter=',')  
  for i in range(1,(NumOfFiles+1)):
      inputfile = "employee_data" + str(i) +".csv"
      input_path = os.path.join("Homework",inputfile)
      with open(input_path,newline='',encoding="utf8") as csvinpfile:
       
         csvreader = csv.reader(csvinpfile,delimiter=',')
         
         next(csvreader,None)
         for bossinp in csvreader:
             changedBoss.append(bossinp[0])
             Names=bossinp[1].split()
             changedBoss.append(Names[0])
             changedBoss.append(Names[1])
             d = datetime.datetime.strptime(bossinp[2], "%Y-%m-%d")
             d = datetime.datetime.strftime(d,"%m/%d/%Y")
             changedBoss.append(d)
             ssn=bossinp[3].split("-") 
             formatedssn = "*** - **-" + ssn[2]
             changedBoss.append(formatedssn)
             changedBoss.append(us_state_abbrev[bossinp[4]])
            ## print(changedBoss)
             csvwriter.writerow(changedBoss)
             changedBoss.clear() 
  