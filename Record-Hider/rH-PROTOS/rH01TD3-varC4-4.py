import os

import json

import time

# contains current file location
wDir_path = os.path.dirname(os.path.realpath(__file__))
#wDir_path = os.getcwd()
 
# File name & File extention (eg: sample,.py)
file_name, file_type = os.path.splitext(os.path.basename(os.path.abspath(__file__)))

# batch files path
hidefl_bat_flname = "{}-opt1_hidefile".format(file_name)

hidefl_bat_fl = "{}.bat".format(hidefl_bat_flname)

bat1_hidefile_flpath = os.path.join(wDir_path,hidefl_bat_fl)

#
hidedir_bat_flname = "{}-opt1_hidefolder".format(file_name)

hidedir_bat_fl = "{}.bat".format(hidedir_bat_flname)

bat1_hidedirs_flpath = os.path.join(wDir_path,hidedir_bat_fl)

#
unhidefl_bat_flname = "{}_opt2-unhidefile".format(file_name)

unhidefl_bat_fl = "{}.bat".format(unhidefl_bat_flname)

bat2_unhidefile_flpath = os.path.join(wDir_path,unhidefl_bat_fl)

#
unhidedir_bat_flname = "{}_opt2-unhidefolder".format(file_name)

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

def rh_batfl_run(batflpath,rh_cmd):
    bat_fl = open(batflpath,"w")

    bat_fl.write(rh_cmd)

    bat_fl.close()

    os.startfile(batflpath)

    delay(2.89)

    os.remove(batflpath)

def json_infos_dump(jsonfl_path,infos):
    json_datas_w = open(jsonfl_path, "a")
                                        
    json.dump(infos, json_datas_w)

    json_datas_w.close()

def rh01TDC42():

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

                    sweep(0)

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

                            print("\n-> Copy and paste the path of the '{0}' file (or leave it as blank if it is at app location ({1})).".format(file,wDir_path))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            fl_path = input("\n.. Paste here -> ")

                            sweep(0)

                            if fl_name=="" or fl_extnts== "":

                                print("\n-> Invalid input")

                                delay(0.12)

                            else:

                                if fl_path =="":
                                    fl_full_path = os.path.join(wDir_path,file)

                                else:
                                    fl_full_path = os.path.join(fl_path,file)

                                fl_exists = os.path.exists(fl_full_path)

                                if fl_exists == False:

                                    print("-> '{}' file not found.".format(file))

                                    delay(0.12)

                                else:

                                    print("\n Hiding file '{}'....".format(file))

                                    cmd1 = 'Attrib +h +s +r "{}"'.format(fl_full_path)

                                    rh_batfl_run(batflpath=bat1_hidefile_flpath,rh_cmd=cmd1)                                  

                                    usr_datas ={
                                            "file_name" : fl_name,
                                            "file_type": fl_extnts,
                                            "file_path" : fl_path
                                            }

                                    json_infos_dump(jsonfl_path=files_datas_jsonflpath,infos=usr_datas)

                                    print("\n\t -> Hide file: Success.")

                                    break

                        elif n==2:

                            json_file_datas_r = open(files_datas_jsonflpath, 'r')

                            data = json_file_datas_r.read()

                            json_flname = json.loads(data)["file_name"]

                            json_flextnts = json.loads(data)["file_type"]

                            json_flpath = json.loads(data)["file_path"]

                            file = "{0}.{1}".format(json_flname,json_flextnts)

                            fl_full_path = os.path.join(json_flpath,file)

                            print("\n Unhiding file '{}'....".format(file))

                            cmd2 = 'Attrib -h -s -r "{}"'.format(fl_full_path)

                            rh_batfl_run(batflpath=bat2_unhidefile_flpath,rh_cmd=cmd2)

                            json_file_datas_r.close()

                            print("\n\t -> Unhide file: Success.")

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

                    sweep(0)

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

                            print("\n-> Copy and paste the path of the '{0}' folder (or leave it as blank if it is at app location ({1})).".format(file,wDir_path))

                            delay(0.18)

                            print("\n-> And then press to 'Enter' button to continue.")

                            delay(0.18)

                            dir_path = input("\n.. Paste here -> ")

                            sweep(0)

                            if dir_name=="":

                                print("\n-> Invalid input")

                                delay(0.12)
                                
                            else:

                                if dir_path =="":

                                    dir_full_path = os.path.join(wDir_path,dir_name)

                                else:
                                    dir_full_path = os.path.join(dir_path,dir_name)

                                dir_exists = os.path.exists(dir_full_path)

                                if dir_exists == False:
                                    
                                    print("\n-> '{}' folder not found.".format(dir_name))

                                else:

                                    print("\n Hiding folder '{}'....".format(dir_name))

                                    cmd1 = 'Attrib +h +s +r "{}"'.format(dir_full_path)

                                    rh_batfl_run(batflpath=bat1_hidedirs_flpath,rh_cmd=cmd1)

                                    usr_datas ={
                                            "dir_name" : dir_name,
                                            "dir_path" : dir_path
                                            }

                                    json_infos_dump(jsonfl_path=dirs_datas_jsonflpath,infos=usr_datas)
                                    
                                    print("\n\t -> Hide folder: Success.")

                                    break

                        elif n==2:

                            json_dirs_datas_r = open(dirs_datas_jsonflpath, 'r')

                            data = json_dirs_datas_r.read()

                            json_dirname = json.loads(data)["dir_name"]

                            json_dirpath = json.loads(data)["dir_path"]

                            dir_full_path = os.path.join(json_dirpath,json_dirname)

                            cmd2 = 'Attrib -h -s -r "{}"'.format(dir_full_path)

                            rh_batfl_run(batflpath=bat2_unhidedirs_flpath,rh_cmd=cmd2)

                            json_dirs_datas_r.close()

                            print("\n\t -> Unhide folder: Success.")

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

    rh01TDC42()

    while True:
        sweep(2.89)

        print("\n>> Type 'n' to exit the app or 'y'.")

        delay(0.18)

        print("\n>> And then press to 'Enter' button to continue.")

        delay(0.18)

        opts = input("\n_>> ").lower()

        sweep(0)

        if opts == 'y':
            rh01TDC42()

        elif opts == 'n':
            break
        else:
            print("\n-> Invalid option.")

        
