import json

from functions import calcDistanceInKm, sortTuplesByFloat

myCoords = ()

taxicabCoords = []
taxicabNameAndDistances = []

# Load the JSON file containing the drivers' data
with open("taxicabData/cabsCoords.json", "r") as file1:
    data = json.load(file1)

# Get my coords from the JSON file
mydata = data["your_coordinates"]
myCoords = (mydata['latitude'], mydata['longitude'])

# Get the list of drivers from the data dictionary
drivers = data['drivers']

# Get the coords
for driver in drivers:
    taxicabCoords.append((driver['latitude'], driver['longitude']))
    distFromTo = calcDistanceInKm(myCoords, (driver['latitude'], driver['longitude'])) 
    taxicabNameAndDistances.append((driver['name'],distFromTo))

# Sort the drivers by distance
taxicabNameAndDistances = sortTuplesByFloat(taxicabNameAndDistances)

# Now make the dictionary list to upload the data to getNearCabs
driversDataToUpload = []
for driver in taxicabNameAndDistances:
    driversDataToUpload.append({"name": driver[0], "distance": driver[1]})

dataToUpload = {
    "taxicabs": driversDataToUpload
}

# Now write the data in the JSON file
with open("taxicabData/getNearCabs.json","w") as file2:
    json.dump(dataToUpload, file2, indent=1)

print("Program finished")
