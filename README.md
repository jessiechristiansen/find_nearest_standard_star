# find_nearest_standard_star
Short python script to read in the IRTF list of telluric standards from the Bright Star Catalog and provide the closest three matches to given coordinates.

The script takes in the coordinates of your object in HHMMSS.S DDMMSS format, and computes the distance to each standard star in the IRTF catalog 
(http://irtfweb.ifa.hawaii.edu/IRrefdata/Catalogs/bsc_a0.dat), which is available in a sanitised-for-pandas version standards.csv, also available from the repository.

I added the designation 'G' to the multiple flag column to indicate 'Good' (no indication of multiplicity).

The script then spits out the distance to the three closest stars, their multiplicity flags, spectral types, and V magnitudes.

Here's an example input and output:

jessiec$ python find_nearest_standard_star.py 01h32m34.34s -12d50m47.7s

3.833720120568216 deg:  HR444  Multiple flag:  G , SpT:  A0III , Vmag =  6.59
27.90645592171924 deg:  HR185  Multiple flag:  W , SpT:  A0V , Vmag =  6.06
29.7289581353242 deg:  HR81  Multiple flag:  G , SpT:  A0V , Vmag =  6.56
