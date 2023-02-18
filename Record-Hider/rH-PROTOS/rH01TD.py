import os

import time


wDir_path = os.path.dirname(os.path.realpath(__file__))# contains current file location
#wDir_path = os.getcwd()
#

hidefl_bat_flname = "recordHider-file_opt1"

hidefl_bat_fl = "{}.bat".format(hidefl_bat_flname)
#

hidedir_bat_flname = "recordHider-folder_opt1"

hidedir_bat_fl = "{}.bat".format(hidedir_bat_flname)
#

unhidefl_bat_flname = "recordHider-file_opt2"

unhidefl_bat_fl = "{}.bat".format(unhidefl_bat_flname)
#

unhidedir_bat_flname = "recordHider-folder_opt2"

unhidedir_bat_fl= "{}.bat".format(unhidedir_bat_flname)


def delay(var):
    time.sleep(var)

def sweep(var):
    time.sleep(var)

    os.system('cls')


def rh01TD():

    while True:

        print("\n>> Type '1' hide/unhide a file.")

        delay(0.19)

        print("\n>> Or type '2' to hide/unhide a folder.")

        delay(0.19)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.19)
        
        m = int(input("\n_> "))

        sweep(0)

        #print(m)

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

                            cmd1 = 'Attrib +h +s +r {}'.format(fl_full_path)

                            bat1_flpath = os.path.join(wDir_path,hidefl_bat_fl)

                            bat1_fl = open(bat1_flpath,"w")

                            bat1_fl.write(cmd1)

                            bat1_fl.close()

                            os.startfile(bat1_flpath)

                            delay(2.89)

                            os.remove(bat1_flpath)

                            print("\n\t -> Success.")


                        elif n==2:
                            print("\n-> Type name of the file you wish to unhide.")

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_name = input("\n Type here -> ")

                            delay(1.8)

                            print("\n-> Type extension of the file (eg: jpg, png, mp4, mp3, wav, docx... etc.)")

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

                            fl_path = input("\n Paste here -> ")

                            sweep(0)

                            fl_full_path = os.path.join(fl_path,file)

                            print("\n Unhiding file '{}'....".format(file))

                            cmd2 = 'Attrib -h -s -r {}'.format(fl_full_path)

                            bat2_flpath = os.path.join(wDir_path,unhidefl_bat_fl)

                            bat2_fl = open(bat2_flpath,"w")

                            bat2_fl.write(cmd2)

                            bat2_fl.close()

                            os.startfile(bat2_flpath)

                            delay(2.89)

                            os.remove(bat2_flpath)

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

                            cmd1 = 'Attrib +h +s +r {}'.format(dir_full_path)

                            bat1_flpath = os.path.join(wDir_path,hidedir_bat_fl)

                            bat1_fl = open(bat1_flpath,"w")

                            bat1_fl.write(cmd1)

                            bat1_fl.close()

                            os.startfile(bat1_flpath)

                            delay(2.89)

                            os.remove(bat1_flpath)

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

                            cmd2 = 'Attrib -h -s -r {}'.format(dir_full_path)

                            bat2_flpath = os.path.join(wDir_path,unhidefl_bat_fl)

                            bat2_fl = open(bat2_flpath,"w")

                            bat2_fl.write(cmd2)

                            bat2_fl.close()

                            os.startfile(bat2_flpath)

                            delay(2.89)

                            os.remove(bat2_flpath)

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

    rh01TD()

    while True:
        #sweep(0)

        print("\n>> Type 'n' to exit the app or 'y' to hide or unhide a file or folder")

        delay(0.18)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.18)

        opts = input("\n_>> ").lower()

        sweep(0)

        if opts == 'y':
            rh01TD()

        elif opts == 'n':
            break
        else:
            print("\n-> Invalid option.")

        
