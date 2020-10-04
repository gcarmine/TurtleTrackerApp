#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Gabrielle Carmine (gabrielle.carmine@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Pretend we read one line of data from the file
lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obvs_date = lineData[2]
obvs_lc = lineData[4]
obvs_lat = lineData[6]
obvs_long = lineData[7]

#Print the location of Sara
print(f"Record {record_id} indicates Sara was seen at lat:{obvs_lat},lon:{obvs_long} on {obvs_date}")
