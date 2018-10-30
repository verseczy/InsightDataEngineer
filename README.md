Problem:
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.
The main task of this project is to create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

Approach:
In this project, it contains two important part:
a) read input file and store them 
I chose "hash" structure which in python the implementation is dictionary to store data from csv input files.
There are two dictionaries, one is for job and the other is for state.
For job dictionary, the key is "OCCUPATIONS" related to SOC code, the value is number of certified applications of these occupations.
For state dictionary, the key is "STATE" and the value is number of certified applications of states.
I chose "mapreduce" method to complete the storaging process to improve performance.
b） sort and choose top 10：
I tried to use merge sort and max heap before, however, the most fastest method is python's build-in function, so I finally chose "sorted" function. 

Run instructions:
under the path ./src and run h1b_counting.py file:
python3 h1b_counting.py

Then the input file is in ./input and the two output files are in ./output

PS:
Because of the large size of input file, I cannot upload input file to github!