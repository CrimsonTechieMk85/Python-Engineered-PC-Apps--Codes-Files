INTRODUCTION
---------------------

'QR Code Generator' an desktop application developed using python 3.6.8 and other add-on libaries. 
Can convert texts\links into QR codes.

QR Code Generator has two parts:
	1) Text or url QR Codes with logo      -  converts texts\links into QR codes.
	2) Text or url QR Codes with logo      -  converts texts\links into QR codes with logo.


Directories&Files
-------------

The QR codes are stored in child folders contained within the 'Collections folder'.

QR codes are generated in 'QR Codes' folder organized in year-month-date folders.

QR codes with logo are generated in 'QR Codes with logo' folder organized in year-month-date folders.

'Collections shortcut' is also made automatically by the application along with child directories ('QR Codes' folder , 'QR Codes with logo' folder ; etc.) .

User is prompt to use a directory to hold the Collections folder' when trying to genarate QR Codes or open 'Collections folder'  (a one-time process, the choosen folder or directory is saved in path json file for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Collections folder'  by reading the values based on respective key.