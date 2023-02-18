import os

import json

import time

# contains current file location
wDir_path = os.path.dirname(os.path.realpath(__file__))
#wDir_path = os.getcwd()

# batch files path
hidefl_bat_flname = "recordHider-file_opt1"

hidefl_bat_fl = "{}.bat".format(hidefl_bat_flname)

bat1_hidefile_flpath = os.path.join(wDir_path,hidefl_bat_fl)

#
hidedir_bat_flname = "recordHider-folder_opt1"

hidedir_bat_fl = "{}.bat".format(hidedir_bat_flname)

bat1_hidedirs_flpath = os.path.join(wDir_path,hidedir_bat_fl)

#
unhidefl_bat_flname = "recordHider-file_opt2"

unhidefl_bat_fl = "{}.bat".format(unhidefl_bat_flname)

bat2_unhidefile_flpath = os.path.join(wDir_path,unhidefl_bat_fl)

#
unhidedir_bat_flname = "recordHider-folder_opt2"

unhidedir_bat_fl= "{}.bat".format(unhidedir_bat_flname)

bat2_unhidedirs_flpath = os.path.join(wDir_path,hidedir_bat_fl)

# Json files path
filedatas_flname_json = 'file_datas'

filesdata_json_fl_name = '{}.json'.format(filedatas_flname_json)

files_datas_jsonflpath = os.path.join(wDir_path,filesdata_json_fl_name)

#
dirsdatas_flname_json = 'folder_datas'

dirsdatas_json_fl_name = '{}.json'.format(dirsdatas_flname_json)

dirs_datas_jsonflpath = os.path.join(wDir_path,dirsdatas_json_fl_name)

def delay(var):
    time.sleep(var)

def sweep(var):
    time.sleep(var)

    os.system('cls')


def rh01TD3A():

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

                            if fl_name=="" or fl_extnts== "" or fl_path=="":

                                print("\n-> Invalid input")

                                delay(0.12)

                            else:
                                fl_full_path = os.path.join(fl_path,file)

                                fl_exists = os.path.exists(fl_full_path)

                                if fl_exists == False:

                                    print("-> '{}' file not found.".format(file))

                                    delay(0.12)

                                else:

                                    print("\n Hiding file '{}'....".format(file))

                                    cmd1 = 'Attrib +h +s +r {}'.format(fl_full_path)

                                    bat1_fl = open(bat1_hidefile_flpath,"w")

                                    bat1_fl.write(cmd1)

                                    bat1_fl.close()

                                    os.startfile(bat1_hidefile_flpath)

                                    delay(2.89)

                                    os.remove(bat1_hidefile_flpath)

                                    usr_datas ={
                                            "file_name" : fl_name,
                                            "file_type": fl_extnts,
                                            "file_path" : fl_path
                                            }

                                    json_file_datas_w = open(files_datas_jsonflpath, "w")
                                        
                                    json.dump(usr_datas, json_file_datas_w)

                                    json_file_datas_w.close()

                                    print("\n\t -> Success.")

                        elif n==2:

                            json_file_datas_r = open(files_datas_jsonflpath, 'r')

                            data = json_file_datas_r.read()

                            json_flname = json.loads(data)["file_name"]

                            json_flextnts = json.loads(data)["file_type"]

                            json_flpath = json.loads(data)["file_path"]

                            file = "{0}.{1}".format(json_flname,json_flextnts)

                            fl_full_path = os.path.join(json_flpath,file)

                            print("\n Unhiding file '{}'....".format(file))

                            cmd2 = 'Attrib -h -s -r {}'.format(fl_full_path)

                            bat2_fl = open(bat2_unhidefile_flpath,"w")

                            bat2_fl.write(cmd2)

                            bat2_fl.close()

                            os.startfile(bat2_unhidefile_flpath)

                            delay(2.89)

                            os.remove(bat2_unhidefile_flpath)

                            json_file_datas_r.close()

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

                            if dir_name==""  or dir_path=="" :

                                print("\n-> Invalid input")

                                delay(0.12)
                                
                            else:

                                dir_full_path = os.path.join(dir_path,dir_name)

                                dir_exists = os.path.exists(dir_full_path)

                                if dir_exists == False:
                                    
                                    print("\n-> '{}' folder not found.".format(dir_name))

                                else:

                                    print("\n Hiding folder '{}'....".format(dir_name))

                                    cmd1 = 'Attrib +h +s +r {}'.format(dir_full_path)

                                    bat1_fl = open(bat1_hidedirs_flpath,"w")

                                    bat1_fl.write(cmd1)

                                    bat1_fl.close()

                                    os.startfile(bat1_hidedirs_flpath)

                                    delay(2.89)

                                    os.remove(bat1_hidedirs_flpath)

                                    usr_datas ={
                                            "dir_name" : dir_name,
                                            "dir_path" : dir_path
                                            }

                                    json_dirs_datas_w = open(dirs_datas_jsonflpath, "w")
                                        
                                    json.dump(usr_datas, json_dirs_datas_w)

                                    json_dirs_datas_w.close()

                                    print("\n\t -> Success.")

                                    break

                        elif n==2:

                            json_dirs_datas_r = open(dirs_datas_jsonflpath, 'r')

                            data = json_dirs_datas_r.read()

                            json_dirname = json.loads(data)["dir_name"]

                            json_dirpath = json.loads(data)["dir_path"]

                            dir_full_path = os.path.join(json_dirpath,json_dirname)

                            cmd2 = 'Attrib -h -s -r {}'.format(dir_full_path)

                            bat2_fl = open(bat2_unhidedirs_flpath,"w")

                            bat2_fl.write(cmd2)

                            bat2_fl.close()

                            os.startfile(bat2_unhidedirs_flpath)

                            delay(2.89)

                            os.remove(bat2_unhidedirs_flpath)

                            json_dirs_datas_r.close()

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

    rh01TD3A()

    while True:
        #sweep(0)

        print("\n>> Type 'n' to exit the app or 'y' .")

        delay(0.18)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.18)

        opts = input("\n_>> ").lower()

        sweep(0)

        if opts == 'y':
            rh01TD3A()

        elif opts == 'n':
            break
        else:
            print("\n-> Invalid option.")

        
