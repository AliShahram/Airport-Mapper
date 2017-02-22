8888888b.                         888 888b     d888          
888   Y88b                        888 8888b   d8888          
888    888                        888 88888b.d88888          
888   d88P  .d88b.   8888b.   .d88888 888Y88888P888  .d88b.  
8888888P"  d8P  Y8b     "88b d88" 888 888 Y888P 888 d8P  Y8b 
888 T88b   88888888 .d888888 888  888 888  Y8P  888 88888888 
888  T88b  Y8b.     888  888 Y88b 888 888   "   888 Y8b.     
888   T88b  "Y8888  "Y888888  "Y88888 888       888  "Y8888  
============================================================================================
Author: Siddharth Sudheer
E-Mail: siddharthsudheer@gmail.com

Co-Author: Ali Shahram Musavi
E-Mail: amusavi15@earlham.edu

Date: February 21, 2017
============================================================================================
* Earlham College
* CS 345 - Software Engineering
* Prof. David Barbella
* Project 1
============================================================================================

-> RUNNING THE PROJECT:

    1) Simply run ./driver.py
      1.1) This will open the GUI

-> Input files:
	- The program takes Airports as the input with connecting flights having a source 
	and destination
	- The input file should have the format:
	Count,    Value,     Destination,     Source
	
	

-> Structure

  => Driver.py:
	It is the core program and other methods are called from here
		...
		
  => graph_app.py:
	Generates the graph and creates the GUI using tkinter
		...
		
  => importer.py:
	Reads the input file and makes it compatible to be used by the rest of the program
		...
		
  => frontend_server.py:
	Takes the data from grap_data and opens a web browser window
		...
		
  => /static/display_graph.js:
	This is the main part of the program that creates the graph
		...
		
  => /templates/index.html:
		...
		
  => /input_files/:
	Has the input files
		...


-> Required Libraries 
	-Pandas need to be installed in the system 

		

-> For more info please read the 'write-up' file or feel free to contact me.
============================================================================================
