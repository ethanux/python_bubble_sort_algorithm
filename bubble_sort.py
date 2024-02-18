
#!/usr/bin/env python

#!/usr/bin/env python

# MIT License
# 
# Copyright (c) [2024] [Ethanux]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Bubble Sort Algorithm in Python

import sys  # Import the sys module to access command-line arguments
import json  # Import the JSON module to work with JSON files

# Function to read the configuration from a JSON file
def read_config(filename):
    with open(filename, 'r') as file:  # Open the JSON file in read mode
        return json.load(file)  # Load and parse the JSON data

#function for the algorithm

def bubblesort(arr) :
	#get the length of elements in the array 
	# get the size of the array as n
	n = len(arr)
	#loop through the array 
	for i in range(n-1):
		swapped = False
		#access each element of the array
		#compare the element found with the next
		# if its grater the switch element position

		for j in range(0, n-i-1):
			#check if the current item is greater tha the next item 
			if arr[j] >= arr[j+1] :

				#swapp the current item with the next item 
				arr[j] , arr[j+1] = arr[j+1], arr[j]

				#swapped becomes true if a swapped is made 
				swapped = True
		#if there are no swapps made
		if swapped == False :
			#exit the loop 
			break

	return arr

# Function to sort either the provided arguments or the default list from the config
def sort_arguments_or_config(*args):

	# Validate input arguments
    for arg in args:
        if not str(arg).isalnum():
            raise ValueError(f"Invalid argument: {arg}. Only alphanumeric characters are accepted.")

    if args:  # If arguments are provided
        unsorted_array = list(args)  # Convert arguments to a list
    else:  # If no arguments provided, use the list from the config
        config = read_config('config.json')
        unsorted_array = config.get('unsorted_array', [])
    
    # Sort the array using bubble sort algorithm
    sorted_array = bubblesort(unsorted_array)
    return sorted_array


if __name__ == '__main__':
    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Remove the script name from the arguments
        args = sys.argv[1:]
        sorted_array = sort_arguments_or_config(*args)  # Pass command-line arguments to the sorting function
        print(f"Sorted array from provided arguments: {sorted_array}")
    else:
        # If no arguments provided, use default list from config
        sorted_array = sort_arguments_or_config()
        print(f"Sorted array from default list: {sorted_array}")
