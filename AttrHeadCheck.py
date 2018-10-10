import re
import sys

#### FILE NAME GOES HERE #### (Working)
csvFileName = sys.argv[-1]

csvfile = open(csvFileName,'r', encoding='utf-8')
csv=[]

try:
	for line in csvfile.readlines():
		csv += [line.split(',')]
	# csv = [line.split(',') for line in csvfile.readlines()]
except:
	print("ERROR: Invalid character. Converting...")
	## WHen we have emojis, we need to convert to utf-8. errors='replace' will replace emojis(or illegal characters) w/ `\uFFD`
	csvfile = open(csvFileName,'r', encoding='utf-8',errors='replace')
	for line in csvfile.readlines():
		## When we find an illegal character we want to replace it with a # rather than the default escape squence: \uFFD
		line.replace(u'\uFFFD','#')
		#Turn the string into an array of strings where each element in the array is gathered by seperating the original string on the commas: joes,ross,rules = [joe,ross,rules]
		csv += [line.split(',')]

###################
## Header Checks ##
###################

## userId Check ## (Working)
Success = False
for i in csv[0]:
	result = re.fullmatch(r"userId",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of userId in Header Row")
else:
	print("Error found - Failure: Invalid formatting of userId in Header Row")


## deviceId Check ## (Working)

Success = False
for i in csv[0]:
	if i == "deviceId":
		Success = True
if Success is True:
	print("Success: Valid formatting of deviceId in Header Row")
else:
	print("Error found - Failure: Invalid formatting of deviceId in Header Row")


## createDisposition Check ## (Working)

Success = False
for i in csv[0]:
	result = re.fullmatch(r"createDisposition",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of createDisposition in Header Row")
else:
	print("Error found - Failure: Invalid formatting of createDisposition in Header Row")


## userAttribute Check ## (Working)

Success = True
# Count = len(csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"userAttributes.([a-zA-Z0-9_ ])+",i)
	if result == None:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of userAttributes in Header Row")
else:
	print(totalErrors, "Error(s) - Failure: Invalid formatting of userAttributes in Header Row")


## Special Characters Check ## (Working)

Success = True
Count = 0 
for i in csv[0]:
	result = re.search(r"(['!@#$%^&*_'])",i)
	if result:
		Success = False
		Count += 1
if Success:
	print("Success: Valid formatting of Header Row (No special characters)")
else:
	print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Special Characters Found)")


## Empty Header Check ## (Working)

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


## userAttributesValuesToAdd Check ## (Working - Same Methodology as userAttributes)

Success = True
# Count = len(csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"userAttributeValuesToAdd.([a-zA-Z0-9_ ])+",i)
	if result == None:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of userAttributeValuesToAdd in Header Row")
else:
	print(totalErrors, "Error found - Failure: Invalid formatting of userAttributeValuesToAdd in Header Row")


## userAttributeValuesToRemove Check ## (Working - Same Methodology as userAttributes)

Success = True
# Count = len(csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"userAttributeValuesToRemove.([a-zA-Z0-9_ ])+",i)
	if result:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of Header Row userAttributeValuesToRemove")
else:
	print(totalErrors,"Error(s) found - Failure: Invalid formatting of userAttributeValuesToRemove")


## userAttributeValuesToIncrement Check ## (Working - Same Methodology as userAttributes)

Success = True
# Count = len(csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"userAttributeValuesToIncrement.([a-zA-Z0-9_ ])+",i)
	if result:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of Header Row userAttributeValuesToIncrement")
else:
	print(totalErrors,"Error(s) found - Failure: Invalid formatting of userAttributeValuesToIncrement")


## unsubscribeCategoriesToAdd Check ## <------ must check ASAP

Success = False
for i in csv[0]:
	result = re.fullmatch(r"unsubscribeCategoriesToAdd",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of unsubscribeCategoriesToAdd in Header Row")
else:
	print("Error found - Failure: Invalid formatting of unsubscribeCategoriesToAdd in Header Row")


## unsubscribeCategoriesToRemove Check ## <------ must check ASAP

Success = False
for i in csv[0]:
	result = re.fullmatch(r"unsubscribeCategoriesToRemove",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of unsubscribeCategoriesToRemove in Header Row")
else:
	print("Error found - Failure: Invalid formatting of unsubscribeCategoriesToRemove in Header Row")


## unsubscribeChannelsToAdd Check ## <------ must check ASAP

Success = False
for i in csv[0]:
	result = re.fullmatch(r"unsubscribeChannelsToAdd",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of unsubscribeChannelsToAdd in Header Row")
else:
	print("Error found - Failure: Invalid formatting of unsubscribeChannelsToAdd in Header Row")


## unsubscribeChannelsToRemove ## <------ must check ASAP

Success = False
for i in csv[0]:
	result = re.fullmatch(r"unsubscribeChannelsToRemove",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of unsubscribeChannelsToRemove in Header Row")
else:
	print("Error found - Failure: Invalid formatting of unsubscribeChannelsToRemove in Header Row")

## newUserId Check ## (Working)

Success = False
for i in csv[0]:
	result = re.fullmatch(r"newUserId",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of newUserId in Header Row")
else:
	print("Error found - Failure: Invalid formatting of newUserId in Header Row")


## Events Check w/ Nested Objects - WIP ## CURRENT WIP

Success = True
# Count = len(csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"events.([a-zA-Z0-9_ ])+",i)
	if result == None:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of event(s) in Header Row")
else:
	print(totalErrors,"Error(s) found - Failure: Invalid formatting of event(s) in Header Row")


## States Check w/ Nested Objects - WIP ## CURRENT WIP

Success = True
# Count = len (csv[0])
totalErrors = 0
for i in csv[0]:
	result = re.fullmatch(r"states.([a-zA-Z0-9_ ])+",i)
	if result == None:
		totalErrors += 1
		Success = False
if Success:
	print("Success: Valid formatting of state(s) in Header Row")
else:
	print(totalErrors,"Error(s) found - Failure: Invalid formatting of state(s) in Header Row")


## Created Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"created",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of created in Header Row")
else:
	print("Error found - Failure: Invalid formatting of created in Header Row")


## lastActive Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"lastActive",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of lastActive in Header Row")
else:
	print("Error found - Failure: Invalid formatting of lastActive in Header Row")


## totalSessions Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"totalSessions",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of totalSessions in Header Row")
else:
	print("Error found - Failure: Invalid formatting of totalSessions in Header Row")


## timeSpentInApp Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"timeSpentInApp",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of timeSpentInApp in Header Row")
else:
	print("Error found - Failure: Invalid formatting of timeSpentInApp in Header Row")


## locale Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"locale",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of locale in Header Row")
else:
	print("Error found - Failure: Invalid formatting of locale in Header Row")


## country Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"country",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of country in Header Row")
else:
	print("Error found - Failure: Invalid formatting of country in Header Row")


## region Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r"region",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of region in Header Row")
else:
	print("Error found - Failure: Invalid formatting of country in Header Row")


## city Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"region",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of city in Header Row")
else:
	print("Error found - Failure: Invalid formatting of city in Header Row")


## location Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"location",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of location in Header Row")
else:
	print("Error found - Failure: Invalid formatting of location in Header Row")


## locationAccuracyType Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"locationAccuracyType",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of locationAccuracyType in Header Row")
else:
	print("Error found - Failure: Invalid formatting of locationAccuracyType in Header Row")


## timezone Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"timezone",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of timezone in Header Row")
else:
	print("Error found - Failure: Invalid formatting of timezone in Header Row")


## timezoneOffsetSeconds ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"timezoneOffsetSeconds",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of timezoneOffsetSeconds in Header Row")
else:
	print("Error found - Failure: Invalid formatting of timezoneOffsetSeconds in Header Row")


## devices Check ## ARRAY OF OBJECTS associated that are nested

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"devices",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of devices in Header Row")
else:
	print("Error found - Failure: Invalid formatting of devices in Header Row")


## devMode Check ##

Success = False
for i in csv[0]:
	result = re.fullmatch(r,"devMode",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of devMode in Header Row")
else:
	print("Error found - Failure: Invalid formatting of devMode in Header Row")