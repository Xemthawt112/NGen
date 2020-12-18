This is the code for a random name generator, using a database of names I found ages ago from somewhere I cannot remember. 
It pulls from a csv and uses tags to narrow the pool it pulls random names from.
Current functionality is:
On request, generates a random full name that is either masculine or feminine using cli.
Loops until user no longer wants to retrieve a name

Future functionality includes:
Addition of new names to be saved to the csv through the cli. 
Addition of new tags to a name to be saved to the csv through the cli.
Additon of batch name request using the cli.
Addition of tag reporting in format using the cli.


To operate, you currently need a copy of python 2.7. Operated by running rannamegen.py with ranname.py and namesource.csv 
in the same folder as python script.