'''
Tells distance from source
author: Nickalas Reynolds
Date: March 2017
'''

# import libraries
from astropy import units as u
import numpy as np


print("Assuming source separations are << distance.")
print("Can input any combination of arcsec separation, distance separation, or distance to source. ")
units = ["au","pc","km","m","lyr","arcsec"]
while True:
	try:
		distance = raw_input("Input distance to source: ")
		separation = raw_input("Input separation/s (csv with arcsec first): ")
		distanceunit = raw_input("Input units of distance [{0}] : ".format(", ".join(str(i) for i in units)))
		separationunit = raw_input("Input units of separation [{0}] : ".format(", ".join(str(i) for i in units)))
	except ValueError:
		continue
	if ((distance != "") or (separation != "")):
		break
separation = separation.split(",")
separationunits = separationunits.split(",")

# function
def len_sepd(lena,dist):
	return ((np.pi / 180.) *  (lena.to(u.arcsec) / 3600.) * dist.to(u.au))
def dist(lena,lend):
	return (lend.to(u.au) / ((np.pi / 180.) *  (lena.to(u.arcsec) / 3600.)))
def len_sepa(lend,dist):
	return (((lend.to(u.au) / dist.to(u.au)) / (np.pi / 180.)) * 3600.)
def callMethod(o, name):
    getattr(o, name)()

# conversion
if distanceunit in units and distance != "":
	for i in range(len(units)-1):
		if distanceunit == units[0]:
			distance = distance * u.au
		if distanceunit == units[1]:
			distance = distance * u.pc
		if distanceunit == units[2]:
			distance = distance * u.km
		if distanceunit == units[3]:
			distance = distance * u.m
		if distanceunit == units[4]:
			distance = distance * u.lyr
if separationunit in units and separation != "":
	for j in range(len(separation)):
		for i in range(len(units)):
			if separationunit[j] == units[0]:
				separation[j]= separation[j]* u.au
			if separationunit[j] == units[1]:
				separation[j]= separation[j]* u.pc
			if separationunit[j] == units[2]:
				separation[j]= separation[j]* u.km
			if separationunit[j] == units[3]:
				separation[j]= separation[j]* u.m
			if separationunit[j] == units[4]:
				separation[j]= separation[j]* u.lyr	
			if separationunit[j] == units[5]:
				separation[j]= separation[j] * u.arcsec

if separationunit in units[0:4] and separation != "":
	if distanceunit in units and distance != "":
		print(len_sepa(separation,distance))
		print("Units arcsec")
	if distance == "":
		print(dis())


#############
# end of code