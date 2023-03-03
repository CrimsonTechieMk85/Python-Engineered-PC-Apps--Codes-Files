INTRODUCTION
---------------------

'Txt2Mp3' an desktop application developed using python 3.6.8 and other add-on libaries. 
Can convert texts into audio (.mp3) files using gTTS (Google Text-to-speech) api module library.

Txt-2-Mp3 has two parts:
	1) Convert      -  converts into audio (.mp3) files.
	2) Play mp3    -   plays exitsing audio files.


Directory
-------------

The audios are stored in 'Audios folder' having orgnized in date-time folders.
'Audios shortcut' is also made automatically by the application.


Files
------

User is prompt to use a directory to hold the 'Audios folder' when trying to convert texts into audios or open 'Audios folder'  (a one-time process, the choosen folder or directory is saved in path json file for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Audios folder'  by reading the values based on respective key.


Process (Text-to-speech)
------------------------------

Please refer image next to this file