INTRODUCTION
---------------------

'Search Online(ver.ChromeSelinium)' is an desktop application developed using python 3.6.8 and other add-on libaries. 
Can browse using chrome driver.

Search Online(ver.ChromeSelinium) has two parts:
	1) Search                    -   browse using chrome browser
	2) Search (incognito)  -  browse using incognito chrome browser


Directory&Files
-------------

User is prompt to choose a chrome driver when trying to browse. (a one-time process, the choosen folder or directory is saved in path json file within the database folder for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"chromedriver_path":"D:\"}].

A 'Log file' is made upon when error occurs after 'Logs' folder is created.