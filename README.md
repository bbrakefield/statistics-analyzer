# Statistical Analyzer

This application is written in Python 3.6!

A cross-platform open source statistics application built using Python's pandas, matplotlib,
numpy, PyQt5, and scipy libraries.

This project is also dependent on Pillow, an extension of the python image library.
This is needed to save images as JPGs.

## Running the Application
To run this program, navigate to the .\statistics-analyzer folder and run:
`python main.py`

 
**Reminder:**
You should be running this application with Python 3.

At the data selection screen you will be able to select which file you wish to import by clicking the "Open File" button and selecting the file.

You must then specify which statistical data type you are working with by selecting either "Ordinal", "Interval", or "Frequency to the left hand side of the screen.

If you wish to select specific columns and rows from a csv file, be sure to specify the starting and ending rows and cloumns in the area below the "Open File" button before choosing your file.

*Note: If you do not wish to import a csv file and instead do manual data entry, click the "Manual Input" button.
How to use manual data entry features will be covered later in this document.*

After you are finished specifying the data you wish to import you may click "OK" to be taken to the appropriate work screen.

Depending on which data type you selected, the screen will look different. For all screens you will see a Calculations group, a Graphs group, and a screen which will be populated with the results of the calculations.

Select which calculations you wish to be see for the data you have imported then press "OK". A report including the results of the calculations you specified will populate the sceen on the right-hand side of the window.

*Some screens may require information from you in order to properly calculate specific stats properly. Use the text fields to supply the application with the proper values.*

To view graphs for the data, specify the type of graph you would like to see in the "Graphs" section and click the "OK" button. A new window will open displaying a graph.
You will be able to navigate through all graphs of a specific type by clicking the "Next" and "Previous" buttons. If you wish to save the graph you are currently viewing you may click the "Save Graph As" button. You may also change the title of the graph beofre doing this by typing the desired name of the graph in the text field under "Change Title" and then clicking the "Change Title" button.

After clicking the "Save Graph As" button you will be taken to a new window where you may specify the name and location of the JPG image you are saving.

If you wish to export the results of your calculations to a CSV file navigate back to menu bar on the work screen. Under "File" you will see "Save As". Clicking this will take you to a window where you will be able to specify the name and location of the CSV file that will contain your results. 

If you wish to save the report generated in the right-hand side window, navigate to "File" on the menu bar and click "Generate Report". This will take you to a window where you will be able to specify the name and location of the TXT file that will contain your report.

## Manual Input
If you specified that you wanted to do manual data entry by clicking the "Manual Input" button on the data input screen, you will be brought to a new window. 

You should first specify which data type you are planning to work with by selecting the type in the drop down menu. Frequency and Interval will only allow you to enter 3 columns. Ordinal will let you to input up to 6 columns of data. For all data types the first row and column should be headers. The rest of the text fields should be numerical values. 

You can change the number of columns and rows by clicking the "-" and "+" buttons.

After entering data, click submit to be taken back to the data import screen and click "OK".
