#!/usr/bin/env python

# Terrible hack written by Mel Chua, Dec 12 2014
# Brittle, undocumented code. Use at your own risk.
# This is designed to take a data CSV
# (whose format I won't bother to specify right now)
# and spit out a js element array for use by Google Charts Timeline.
# Yes, I'm breaking a bazillion principles of good sw dev.
# This is not good sw dev, it's a hack so I can demo quickly.

infile = open("C:\data.csv","r")
rawdata = infile.readlines()
data = []
for item in rawdata:
  data += [item.split("#")]

def format(input):
  output = ""
  output += "[ '"
  output += input[0] # File
  output += "', '"
  output += input[1] # Header
  output += "', new Date("
  output += input[2] # Year start
  output += ","
  output += input[3] # Month start
  output += ","
  output += input[4] # Day start
  output += "), new Date("
  output += input[5] # Year start
  output += ","
  output += input[6] # Month start
  output += ","
  output += input[7] # Day start
  output += "), '"
  output += input[8].rstrip() # Raw data
  output += "' ]"
  return output
  
outfile = open("C:\output.txt","w")

for line in data:
  outfile.write(format(line))
  outfile.write(",\n")
