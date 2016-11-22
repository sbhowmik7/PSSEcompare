# PSSEcompare
DESCRIPTION:
Compare PSS®E sav or raw files using python and output difference in excel or py files.This is the commandline version 
based on Gridcompare (whit.com.au) with the added fuctionality to include raw files as inputs to be compared.

HISTORY: 
While trying to compare various PSS®E files I found that Gridcompare kept crashing and it was getting to be a pain
in trying to debug the JSON and bottle calls. I decided to create a commandline version of this excellent tool.
PSS®E33.0 to PSS®E33.8 had a bad "caspy.Savefile()" module which was leading to the crashes.

USAGE:
the main file is runPSSECompare.py. Modify this to change the default inputs to or use the command line version
python -m runPSSEcompare -o <Originalfile> -c <File2compare> -x[WriteoutExcelFile]

MODIFICATION:
Use app_settings.py to change some of the paths as well as some of the settings

NOTES:
Uses subprocess (with caspy) in case caspy causes python to crash. If so it tries to use psspy modules
to access the data within the input files.

USES: 
Public modules/library:
certifi
chardet
openpyxl
orderdict

Other:
pssepath


TESTED:
Tested on Windows with PSS®E 33/32/31 and their respective python versions (2.7,2.5)

email: sbhowmik at rocketmail dot com
