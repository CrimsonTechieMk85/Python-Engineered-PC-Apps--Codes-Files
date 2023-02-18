import os

import time


def delay(var):
    time.sleep(var)

def sweep(var):
    time.sleep(var)

    os.system('cls')


def rh00():

    while True:

        print("\n>> Type '1' hide/unhide a file.")

        delay(0.19)

        print("\n>> Or type '2' to hide/unhide a folder.")

        delay(0.19)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.19)
        
        m = int(input("\n_> "))

        sweep(0)

        print(m)

        if m == "":
            print("\n-> Input invalid.")

            delay(0.12)

        else:
            if m==1:
                while True:
                
                    print("\n>> Type '1' to hide a file.")

                    delay(0.18)

                    print("\n>> Or type '2' to unhide a file.")

                    delay(0.18)

                    print("\n>> And then press to 'Enter' button to continue.")

                    delay(0.18)
                    
                    n = int(input("\n_> "))

                    if n=="":

                        print("-> Invalid input")

                        delay(0.12)

                    else:

                        if n==1:
                    
                            print("\n-> Type name of the file you wish to hide.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_name = input("\n Type here -> ")

                            delay(1.8)

                            print("\n-> Type extension of the file (eg: jpg, png, mp4, mp3, wav... etc.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_extnts = input("\n Type here -> ")

                            file = "{0}.{1}".format(fl_name,fl_extnts)

                            sweep(1.18)

                            print("\n-> Copy and paste the path of the '{}' file.".format(file))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_path = input("\n.. Paste here -> ")

                            sweep(0)

                            fl_full_path = os.path.join(fl_path,file)

                            print("\n Hiding file '{}'....".format(file))

                            os.system("cmd /c 'Attrib +h +s +r {}'".format(fl_full_path))

                            print("\n\t -> Success.")

                        elif n==2:
                            print("\n-> Type name of the file you wish to unhide.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_name = input("Type here -> ")

                            delay(1.8)

                            print("\n-> Type extension of the file (eg: jpg, png, mp4, mp3, wav... etc.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_extnts = input("Type here -> ")

                            file = "{0}.{1}".format(fl_name,fl_extnts)

                            sweep(1.18)

                            print("\n-> Copy and paste the path of the '{}' file.".format(file))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_path = input("\n Paste here -> ")

                            sweep(0)

                            fl_full_path = os.path.join(fl_path,file)

                            print("\n Unhiding file '{}'....".format(file))

                            os.system("cmd /c 'Attrib -h -s -r {}'".format(fl_full_path))

                            print("\n\t -> Success.")

                            break
                        else:

                            print("\n-> Invalid input")

                            delay(0.12)
                        break

            elif m==2:
                while True:
                    
                    print("\n>> Type '1' to hide a folder.")

                    delay(0.18)

                    print("\n>> Or type '2' to unhide a folder.")

                    delay(0.18)

                    print("\n>> And then press to 'Enter' button to continue.")

                    delay(0.18)
                    
                    n = int(input("\n_> "))

                    if n=="":

                        print("\n-> Invalid input")

                        delay(0.12)

                    else:

                        if n==1:
                            print("\n-> Type name of the folder you wish to hide.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            dir_name = input("\n Type here -> ")

                            print("\n-> Copy and paste the path of the '{}' folder.".format(dir_name))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            dir_path = input("\n.. Paste here -> ")

                            sweep(0)

                            dir_full_path = os.path.join(dir_path,dir_name)

                            print("\n Hiding folder '{}'....".format(dir_name))

                            os.system("cmd /c 'Attrib +h +s +r {}'".format(dir_full_path))

                            print("\n\t -> Success.")

                            break

                        elif n==2:

                            print("\n-> Type name of the folder you wish to unhide.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            dir_name = input("\n Type here -> ")

                            sweep(1.18)

                            print("\n-> Copy and paste the path of the '{}' folder.".format(dir_name))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            dir_path = input("\n.. Paste here -> ")

                            sweep(0)

                            dir_full_path = os.path.join(dir_path,dir_name)

                            print("\n Unhiding folder '{}'....".format(dir_name))

                            os.system("cmd /c 'Attrib -h -s -r {}'".format(dir_full_path))

                            print("\n\t -> Success.")

                            break

                        else:

                            print("-> Invalid input")

                            delay(0.12)
                        break

            else:

                print("\n-> Invalid input")

                delay(0.12)

            break
                    

if __name__=='__main__':

    rh00()

    while True:
        #sweep(0)

        print("\n>> Type 'n' to exit the app or 'y' to hide or unhide a file or folder")

        delay(0.18)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.18)

        opts = input("\n_>> ").lower()

        sweep(0)

        if opts == 'y':
            rh00()

        elif opts == 'n':
            break
        else:
            print("\n-> Invalid option.")

        
