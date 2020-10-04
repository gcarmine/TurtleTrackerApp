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

#Ask user for the search date
user_date = input("Enter date to search for Sara: ")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionaries
date_dict = {}
coord_dict = {}

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
    
    #Print the location of Sara if lc is 1, 2, or 3
    if obvs_lc in ("1","2","3"):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obvs_lat},lon:{obvs_long} on {obvs_date}")
        date_dict[record_id] = obvs_date
        coord_dict[record_id] = (obvs_lat,obvs_long)
        
#Create an empty list to hold matching keys
matching_keys = []

#Loop through items in the date_dict, and collect keys for matching ones
for date_item in date_dict.items():
    #Get the key and date of the dictionary item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date:
        #If so, add key to the list
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching keys
for matching_key in matching_keys:
    obvs_lat, obvs_long = coord_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obvs_lat},lon:{obvs_long} on {user_date}")