# Taxicabs Locator 🏙🚕
Given the cabs coordinates and it's driver's names in a .JSON file which can be real-time updated, taxi data is uploaded, sorted by distance.

## Step by Step
First of all, the coordinates of taxicabs in a specific area are needed. I asked the AI [ChatGPT](https://chat.openai.com/chat) to fill the cabsCoords.json file with the coords of seven random taxis around Manhattan, NYC. And to limit it a bit more, from the Central Park to the south. ChatGPT also named the drivers and gave me my coords at the intersection of Broadway and W 30th St.
```
{
"your_coordinates": {
     "latitude": 40.74682811843807, 
     "longitude": -73.98848619172874 },
"drivers": [
      { "name": "John Smith", "latitude": 40.74771308973833, "longitude": -73.97877709492026 },
      { "name": "Sarah Johnson", "latitude": 40.752075100489364, "longitude": -74.00084177004521 },
      ...
      { "name": "William Wang", "latitude": 40.74083180050023, "longitude": -74.00535973627026 }
    ]
  }
```
