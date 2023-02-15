from math import sin, cos, asin, sqrt, radians

# Calculate the great circle distance (in kilometers) between two points
# on the Earth's surface given their latitude and longitude coordinates.
def calcDistanceInKm(coord_A, coord_B):
    # Unpack latitude and longitude coordinates for each point
    lat1, lon1 = coord_A
    lat2, lon2 = coord_B
    
    # Convert latitude and longitude to radians
    # Map function applies the given function (radians) to every element
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Calculate distance using the Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of the Earth in kilometers
    distance = c * r
    
    return distance

def sortTuplesByFloat(arr):
    # Sort the tuples based on the float value, the second element of each one.
    # I use it to sort the distances array and stay with their names

    sorted_arr = sorted(arr, key=lambda x: x[1])
    return sorted_arr