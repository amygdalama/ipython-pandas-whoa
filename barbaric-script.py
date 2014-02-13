import csv
import pprint
import urllib2

import matplotlib.pyplot as plt


url = "http://mlr.cs.umass.edu/ml/machine-learning-databases/iris/iris.data"

# Open data from URL as a file-like object
f = urllib2.urlopen(url)

# Create an empty list to store our data
parsed_data = []

# Read file
raw_data = csv.reader(f)

# Define our headers since the file doesn't contain explicit headers
# I found these headers from looking at the documentation at
# http://mlr.cs.umass.edu/ml/machine-learning-databases/iris/iris.names
headers = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class'
	]

# Iterate through the rows in the file, and create a dictionary for each row
for row in raw_data:

	# Dictionaries should have headers -> row
	parsed_data.append(dict(zip(headers, row)))

# Delete the last row of parsed_data because it's blank
parsed_data = parsed_data[:-1]

# Let's see what parsed_data looks like
pprint.pprint(parsed_data[:3])

# Let's create a list of the Sepal Lengths
# I'm calling float on the entries because otherwise they're stored as strings
sepal_lengths = [float(parsed_data[i]['Sepal Length']) 
		for i in range(len(parsed_data))]

plt.hist(sepal_lengths, color='#348ABD', edgecolor='none')
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.show()