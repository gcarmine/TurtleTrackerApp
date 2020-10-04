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

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Iterate through all lines in the line list
for lineString in line_list:
    if lineString[0] in ("#","u"): continue

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
