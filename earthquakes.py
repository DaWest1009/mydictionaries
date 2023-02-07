'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.
NOTE: No hard-coding allowed except for keys for the dictionaries
1) print out the number of earthquakes
2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.
3) using the eq_dict dictionary, print out the information as shown below (first 
three shown):
Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364
Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604
Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628
'''
import json

infile = open('eq_data.json', 'r')
eqData = json.load(infile)

#Part 1 print out the number of earthquakes
print('\n', "Number of earthquakes: ", len(eqData['features']) ,'\n', sep='')

#Part 2 iterate through the dictionary and extract data, and save it in a new dictionary
eq_dict =  {}
count = 1

for eq in eqData['features']:
   if eq['properties']['mag'] > 6:
      eq_dict["Eq" + str(count)] = {}
      eq_dict["Eq" + str(count)]["Loc"] = eq['properties']['place']
      eq_dict["Eq" + str(count)]["Mag"] = eq['properties']['mag']
      eq_dict["Eq" + str(count)]["Lon"] = eq['geometry']['coordinates'][0]
      eq_dict["Eq" + str(count)]["Lat"] = eq['geometry']['coordinates'][1]
      count += 1

#print out new dictionary
print("New Dictionary: ", '\n', eq_dict, '\n')

#Part 3 using the eq_dict dictionary, print out the information
for keys in eq_dict:
   print("Location: ", eq_dict[keys]["Loc"], "\nMagnitude: ", eq_dict[keys]["Mag"], 
   "\nLongitude: ", eq_dict[keys]["Lon"], "\nLatitude: ", eq_dict[keys]["Lat"], sep='')









   
   

   


   
