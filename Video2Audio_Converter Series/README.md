INTRODUCTION
---------------------

'Vido 2 Audio : The converter' is an desktop application developed using python 3.6.8 and other add-on libaries. 
Converts video file into audio file.

Vido 2 Audio : The converter has two modes:
	1) Single file      -  Convert one video file into audio file.
	2) Multiple files -  Convert more than one video files into audio files.


Directory
-------------

The audios are stored in 'Audios folder' having orgnized in Year-Month-Date folders.
'Audios folder shortcut' is also made automatically by the application.


Files
------

User is prompt to use a directory to hold the 'Audios folder' when trying to convert a video into audio or to open 'Audios folder'  (a one-time process, the choosen folder or directory is saved in path json file for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Audios folder' by reading the values based on respective key.