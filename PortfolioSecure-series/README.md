INTRODUCTION
---------------------

'Portfolio Secure' is an desktop application developed using python 3.6.8 and other add-on libaries. 
Can secure files or folders by encrypting into a unreadable file (.enc) .

Portfilio secure has two parts:
	1) Folder Guardian - converts folders into unreadable file (.enc)
	2) File Guardian     -   converts files into unreable file (.enc)


PASSWORDS
---------------------

Passwords are customizable and hashed for enhanced security. These hashed passwords are saved into json file as a container.
These hashed passwords act as' lock-and-key' pair to access 'Portfolio Secure' encryption\decryption features and settings modification.

Intial (default) passwords are as follows:
	1) Folder Guardian:
		i)  Encryption password:  13
		ii) Decryption password:  12
	2) File Guardian:
		i)  Encryption password:  23
		ii) Decryption password:  22


Note: Please be advised using default passwords offers less protection. So kindly change passwords to have high security after installation.


Directory
-------------

Encrypted files are saved in 'Encrypted files' and decrypted files are saved in 'Decrypted files'.

Same goes for folder as well, encrypted folders are saved in 'Encrypted folders' and decrypted folders are saved in 'Decrypted folders'.

These folders are stored in 'Collection folder' having orgnized date-time folders. 'Collection shortcut' is also made automatically by the application.

A 'Database' folder is made upon app startup containing a 'Settings' and 'Backup' folders.


Files
------

A password json is gernerated containing default passwords (enctyption\decryption passwords) upon app startup. 

User is prompt to use a directory to hold the 'Collection folder' when trying to encrypting\decrypting  a file or folder (a one-time process, the choosen folder or directory is saved in path json file within the database folder for later use).

The json file use dictionaries containing 'Key-Value' pairs to save\update\read datas [Eg: {"path":"D:\"}].

Using path json file, the app generates 'Collection folder' by reading the values based on respective key.

Using password json file, the app gets the passwords for encryption and decryption by reading the values based on thier respective keys.


Process (Encyption\Decryption)
------------------------------

Please refer image next to this file