#Updates made as of 15-Aug-2018
#Added sys argument to remove need to change file name in script (thanks Jon!)
#Added enumerate to get the index for data row checks - prints exact row the issue stems from (also thanks to Jon!)
#Now with threading! (it's slightly more efficient!)
#Implemented progress bar (and eliminated excess information from progress bar)
print("")
print("Beginning scan of CSV file")
print("")
print("Preparing file...")
print("")

import re
import time, sys
import threading
from threading import Thread

#### FILE NAME GOES HERE ####
csvFileName = sys.argv[-1]

csvfile = open(csvFileName,'r', encoding='utf-8')
csv=[]
#if ascii_decode error thrown, try utf-8 encoding
try:
	csv = [line.split(',') for line in csvfile.readlines()]
except:
	print("ERROR: Invalid character. Converting...")
	csvfile = open(csvFileName,'r', encoding='utf-8',errors='replace')
	for line in csvfile.readlines():
		line.replace(u'\uFFFD','#')
		csv += [line.split(',')]

#progress bar
def update_progress(progress):
	barLength = 10 # Modify this to change the length of the progress bar
	status = ""
	if isinstance(progress, int):
		progress = float(progress)
	if not isinstance(progress, float):
		progress = 0
		status = "error: progress var must be float\r\n"
	if progress < 0:
		progress = 0
		status = "Halt...\r\n"
	if progress >= 1:
		progress = 1
		status = "Done...\r\n"
	block = int(round(barLength*progress))
	text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
	sys.stdout.write(text)
	sys.stdout.flush()


#Check for Valid File Name with no special characters (PLACE YOUR FILE NAME IN HERE)
def CheckFileName():
	Success = True
	for i in csvFileName:
		result = re.search(r"(['!@#$%^&*_ '])",i)
		if result:
			Success = False
	if Success:
		print("Success: Valid File Name")
	else:
		print("Failure: Invalid File Name (Cannot have special characters or spaces)")	

#############################
##### HEADER ROW CHECKS #####
#############################	

	#Column check 200 limit
def CheckLimit():
	csvfile = open(csvFileName,'r')
	for row in csvfile:
		if len(row) <= 200:
			print("Success: CSV has", len(row), "rows.")
		elif len(row) > 200:
			print("Error: CSV has", len(row), "rows.")
		break	

	#Check if header-userId is formatted correctly
def CheckUserId():
	Success = False
	for i in csv[0]:
		result = re.fullmatch(r"userId",i)
		if result:
			Success = True
	if Success:
		print("Success: Valid formatting of userId in Header Row")
	else:
		print("Error found - Failure: Invalid formatting of userId in Header Row")	

	#Check if header-userAttributes formatted correctly
def CheckHeadAttribute():
	Success = False
	Count = len(csv[0])-1
	for i in csv[0]:
		result = re.fullmatch(r"userAttributes.([a-zA-Z0-9_ ])+",i)
		if result:
			Success = True
	if Success:
		print("Success: Valid formatting of Header Row userAttribute(s)")
	else:
		print(Count,"Error(s) found - Failure: Invalid formatting of userAttribute(s)")	

	#Check if there is empty header item <-- To Do (Understand what the hell is going on here)
def EmptyHeadCheck():
	Success = True
	blank = re.compile(r'\s*')
	Count = 0
	for i in csv[0]:
		result = blank.match(i).end() == len(i)
		if result:
			Success = False
			Count += 1
	if Success:
		print("Success: Valid formatting of Header Row (No empty header column)")
	else:
		print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Empty header column(s) found")	

	#Check if there are special characters in header row
def CheckSpecChar():
	Success = True
	Count = 0 
	for i in csv[0]:
		result = re.search(r"(['!@#$%^&*_ '])",i)
		if result:
			Success = False
			Count += 1
	if Success:
		print("Success: Valid formatting of Header Row (No special characters)")
	else:
		print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Special Characters Found)")	

	###########################
	##### DATA ROW CHECKS #####
	###########################	
def CheckRowLength():
	Success = True
	Count = 0
	Errors = []
	for num, i in enumerate(csv[1:],start = 2):
		result = len(i) > len(csv[0])
		if result:
			Success = False
			Count += 1
			Errors.append(num)
	if Success:
		print("Success: Valid Data Row length")
	else:
		print(Count,"Error(s) found - Failure: Data Row longer than Header Row - Errors found in the following rows:", Errors)

# update_progress test script
print("Scan in progress : Standby...")
for i in range(100):
	time.sleep(0.1)
	update_progress(i/100.0)
print("")

print("")
print("Success: Scan complete - Compiling results...")
time.sleep(10)
print("")
print("Scan Results:")

if __name__ == '__main__':
	Thread(target = CheckFileName).start()
	Thread(target = CheckLimit).start()
	Thread(target = CheckUserId).start()
	Thread(target = CheckHeadAttribute).start()
	Thread(target = EmptyHeadCheck).start()
	Thread(target = CheckSpecChar).start()
	Thread(target = CheckRowLength).start()
