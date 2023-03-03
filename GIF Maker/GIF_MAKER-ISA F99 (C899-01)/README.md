INTRODUCTION
---------------------

'GIF Maker' is an desktop application developed using python 3.6.8 and other add-on libaries. 
Can generate GIF from pictures.

Directories&Files
-------------------

These Gif files are stored in 'Collection folder' having organized date folders. 
'Collection shortcut' is also made automatically by the application.
 
User is prompt to use a directory to hold the 'Collection folder' when trying to generate a gif file or accessing 'Collection folder' (a one-time process, the choosen folder or directory is saved in path json file for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Collection folder' by reading the values based on respective key.
