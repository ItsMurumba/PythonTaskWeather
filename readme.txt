#Kelvin Murumba
#Weather.py documentation
#10/04/2017

Weather.py is a script that will give you the day of the month with the maximum difference as compared to the other days based on the MxT and MnT.

The script is divided into four main functions:
    1. Constructor that represents an instance of the object itself. This is where relevant values have beed initialized namely most_diff, open_file
    2. Open file function, opens the weather.dat file which will be the source of data to be used in the script.
    3. Read function.The function reads the keys and values of data from the opened file. The needed columns only i.e Dy, MxT and MnT are read in this
        together with their values. The data is then appended to a list after being zipped.
    4. The function is used to get the maximum valued day based on the differences between the min and max temperatures. The function checks the inputs
        if they are digits and converted to nfloat to accomodate decimals. The dummy dictionary is used to hold the day and the difference in temperatures.
        The dictionery with the differences is then sorted in descending order. The day that occupies the 0th position in the sorted list is the one with
        the largest difference.
