INTRODUCTION
---------------------

'MySQL2Excel_Exporter' is an desktop application developed using python 3.6.8 and other add-on libaries. 
The application exports MySql tables as a excel file.

MySQL2Excel_Exporter has two parts:
	1) Export           -  converts all records in mySQL table into excel file
	2) Export Filter  -  converts selected recorerds in mySQL table into excel file


Directory&Files
----------------------

'Ouput' excel files are saved and organized in year-month-date folders in 'Excel files' folder

User is prompt to use a directory to hold the 'Excel files folder' when trying to export mysql  as a excel file (a one-time process, the choosen folder or directory is saved in path json file for later use).

User is prompt to enter thier mySQL credentials such as host name, user name, password, database name and table name (a one-time process, credentials saved in credential json file for later use)

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Excel files folder' by reading the values based on respective key.

Using credential json file, the app gets the mySQL credentails by reading the values based on thier respective keys.
