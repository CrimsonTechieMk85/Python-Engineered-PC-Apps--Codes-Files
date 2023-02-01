from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time
import sys
import shutil

#cdir = os.getcwd()
cdir = os.path.dirname(os.path.realpath(__file__))

def wipeout(val):

    time.sleep(val)

    os.system('cls')

def delay(var):
    time.sleep(var)

def v2a08():

    while True:
    # ---> user interface - test

        # video name

        print("\nType the name of the video file down below.")

        delay(0.18)

        print("\nAnd then press 'Enter' to continue.")

        delay(0.18)
        
        video_name = input("\n_>> ")

        wipeout(0.45)

    # video path

        print("\nCopy the path where your '{}' video file down below.".format(video_name))

        delay(0.18) 

        print("\nAnd then press 'Enter' to continue.")

        delay(0.18)

        video_path = input("\n_>> ")

        wipeout(0.45)
        
    # video format

        print("Type the format (extension) of the folder video file download (for example like this: mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov, webm). \n")

        delay(0.18)

        print("\nAnd then press 'Enter' to continue.")

        delay(0.18)
            
        video_format = input("\n_>> ")

        wipeout(0.45)

    #---> file and paths
            
        src_video_file = "{0}.{1}".format(video_name,video_format)

        source_video_path = os.path.join(video_path,src_video_file)

        source_audio_path = source_video_path.replace(".mp4",".mp3")

        final_video_path = os.path.join(cdir,src_video_file)

        final_mp3_fl = "{0}.{1}".format(video_name,"mp3")

        final_mp3_path = os.path.join(cdir,final_mp3_fl)

        final_mp3_exists= os.path.exists(final_mp3_path)

        src_video_file_exists = os.path.exists(source_video_path)

        #
        if video_name =="" or video_path=="" or video_format=="":

            print("Invalid input.")

            wipeout(2.89)

        else:

            if src_video_file_exists is True:
                
                if final_mp3_exists is True:

                    print("\n-> Audio file '{}.mp3' already exists.".format(video_name))

                    wipeout(2.89)

                else:

                #---> video-audio conversion 

                    if "mp4" in video_format:

                        try:
                            my_clip =VideoFileClip(source_video_path)

                            my_clip.audio.write_audiofile(final_mp3_path)

                            my_clip.close()

                            print("\n->  Successfully converted '{}' video into audio file.".format(video_name))

                            break

                        except KeyError:
                            try:
                                shutil.copyfile(source_video_path, final_video_path) 
                            except shutil.SameFileError:
                                os.remove(final_video_path)
                                            
                            os.rename(final_video_path,final_mp3_fl)

                            print("\n->  Successfully converted '{}' video into audio file.".format(video_name))

                        except FileNotFoundError:

                            try:
                                os.remove(final_video_path)
                            except OSError:
                                pass

                            break
                        except Exception:

                            try:
                                os.remove(final_video_path)
                            except OSError:
                                pass

                            break

                            
                    else:
                        try:
                            shutil.copyfile(source_video_path, final_video_path) 
                        except:
                            os.remove(final_video_path)
                                        
                        try:
                            rename_into_mp4_file = final_video_path.replace(video_format,'.mp4')
                            final_mp3_file = rename_into_mp4_file.replace('.mp4','.mp3')

                            os.rename(final_video_path,rename_into_mp4_file)

                            my_clip =VideoFileClip(rename_into_mp4_file)
                            my_clip.audio.write_audiofile(final_mp3_file) 

                            my_clip.close()

                            os.remove(rename_into_mp4_file)

                            print("\n->  Successfully converted '{}' video into audio file.".format(video_name))

                            break

                        except FileNotFoundError:

                            try:
                                os.remove(final_video_path)
                            except OSError:
                                pass

                            print("\n-> Successfully converted '{}' video into audio file.".format(video_name))

                            break

                        except Exception:
                            try:
                                os.remove(final_video_path)
                            except OSError:
                                pass

                            print("\n-> Successfully converted '{}' video into audio file.".format(video_name))

                            break
            else:

                print("\n-> '{}' video file not found in the given path.".format(video_name))
    #   
            
if __name__=='__main__':
    v2a08()

    while True:
        print("\nDo you wish to use the app again?")

        opts = input("\nY/y or N/n >> ").lower()

        #wipeout(0.12)

        if "y" == opts:

            wipeout(0.12)

            #print("\n<___________________________________________________>")

            v2a08()
            
        elif "n" == opts:
            #sys.exit()
            break
        else:
            print("Option invalid.")

            wipeout(2.83)


