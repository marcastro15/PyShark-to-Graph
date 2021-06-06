# PyShark-to-Graph-Visual-Network-Graph-Analyzer

This network-graph analyzer gives visual representation of data captured from WireShark (pcap file) or any similar compatible file format. The captured data will covert the text into maps, graphs, charts, and etc. To put this into perspective, it is the taking information (data) and placing it into a visual context, such as a map or graph. Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data. In the early days, the easiest and most common way to create a data visualization was to take the information from an Excel spreadsheet and transform it into a bar graph, pie chart, or table. This method is still extremely effective, but the art of data visualization has also come a long way in the past 20+ years. Nowadays, you also have the option to create more intricate visualizations such as Bubble clouds, Bullet graphs, Readial trees, and etc. using Pyshark and Matplotlib library.

Why do we care?
---------------
1. Data visualizations make big and small data easier for the human brain to understand, and visualization also makes it easier to detect patterns, trends, and outliers in groups of data.
2. Data visualization is the act of taking information (data) and placing it into a visual context, such as a map or graph. Data visualizations make big and small data easier for the human brain to understand, and visualization also makes it easier to detect patterns, trends, and outliers in groups of data.
3. Forensic analysis detailed investigation for detecting and documenting the course, reasons, culprits, and consequences of a security incident or violation of rules of the organization or state laws. It would be easier to visualize the data in graphical representation than reading text.

Requirements
------------
- Any Linux environment
- Knowledge of Wireshark
- Knowledge of Python, Matplotlib

Installation
------------
1. sudo apt-get update
2. sudo apt-get install python3.6
3. sudo apt install python3-pip
4. pip3 install python-csv
5. pip3 install pyshark
6. pip3 install matplotlib
7. pip3 install thread

How to run it?
--------------
1. Get the data source from WireShark (pcap format)
2. python3 ./nets_visualizer.py
Note that the syntax used is compatible only to python3 version.

Future Work
-----------
Many small and medium business with IT infrastructure that do not have budget to create visual network analyzer should delve into development components for easy transition from “raw data” to pictorial diagram of the Wireshark's data.There are many modules/libraries available to create visual data derived from PyShark, but it needs lots of formatting to be compatible. As a result, PyShark must have a module to convert to more data format that are consumable by other modules to present visual data.


 





 
