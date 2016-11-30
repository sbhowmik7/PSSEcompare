# PSSEcompare
<b>DESCRIPTION:</b>
Compares PSS®E sav or raw files using python and output difference in excel or py files.This is the commandline version 
based on [Gridcompare] (http://www.whit.com.au/gridcompare/) with the added fuctionality to include raw files as inputs to be compared.

<b>HISTORY:</b> 
While trying to compare various PSS®E files I found that Gridcompare kept crashing and it was getting to be a pain
in trying to debug the JSON and bottle calls in its browser based comparisons. I decided to create a commandline version of this excellent tool.

PSS®E 33.0 to PSS®E 33.8 had a bad "caspy.Savefile()" module which was leading to the crashes.

<b>USAGE:</b>
the main file is <i> runPSSECompare.py</i>. Modify this to change the default inputs to or use the command line version
> python -m runPSSEcompare -o {Originalfile} -c {File2compare} -x[WriteoutExcelFile]

<b>MODIFICATION:</b>
Use *app_settings.py* to change some of the paths as well as some of the settings

<b>NOTES:</b>
Uses subprocess (with caspy) in case caspy causes python to crash. If so it tries to use psspy modules
to access the data within the input files. Use of caspy can be done with just PSSE installed and does not 
require a dongle to work which is advantageous if one has an hourly license.
On really large files like the eastern interconnect (>60K buses) it takes a really large time and might crash due to size constraint on the sqlite databases.

<b>USES:</b> 
Public modules/library:
* openpyxl
* orderdict

<b>Other:</b>
pssepath


<b>TESTED:</b>
Tested on Windows with PSS®E 33/32/31 and their respective python versions (2.7,2.5)

__email:__ *sbhowmik at rocketmail dot com*
