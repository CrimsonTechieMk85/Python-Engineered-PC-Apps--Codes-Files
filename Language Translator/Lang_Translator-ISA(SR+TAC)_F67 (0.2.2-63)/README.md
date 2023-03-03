INTRODUCTION
---------------------

'Language Translator' is an desktop application developed using python 3.6.8 and other add-on libaries. 
Can Tranlate any language and convert translated text into audio.


Directory&Files
--------------------

User is prompt to use a directory to hold the 'Collection folder' or  when trying to translate (a one-time process, the choosen folder or directory is saved in path json file within the database folder for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Collection folder' by reading the values based on respective key.

'Logs' folder and Log is generated at application location when a error occurs.


Process info - Translation
----------------

When 'translate' button is clicked, the text to be translated (typed in the input field) is converted into desired language using 'google_trans' api library with the requested text and desired language (Choosed form the combobox) as input.

Then the translated text is later saved as audio using 'gTTS' api library.

The 'translated texts' and 'translated text audios' are saved in 'Output records' and 'Output audios' folders respectively.

Texts can be alo be captured using 'Speech Recognition' and translated when user forgets\does not wish to type the text in input field .

Speech recognized texts are also saved as audio using 'gTTS' api library.
