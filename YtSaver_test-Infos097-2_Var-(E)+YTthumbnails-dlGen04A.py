import re
from pytube import YouTube , Channel , Playlist
import time
import os
import sys
import json
import requests

# Get full file path - real path
wfile_realpath = os.path.realpath(__file__)

# Get full file path - absolute path
wfile_abspath = os.path.abspath(__file__)

# Get file name & file extension
file_name, file_extnts = os.path.splitext(os.path.basename(wfile_realpath))

# Get current file path using realpath
cpath1 = os.path.dirname(wfile_realpath)

print("\n-> Folder realpath [os.path.realpath(__file__)]: \n"+cpath1)

# Get current file path using abspath
cpath2 = os.path.dirname(wfile_abspath)

print("\n-> Folder realpath [os.path.abspath(__file__)]: \n"+cpath2)

# Get current file path using get current directory
cpath3 = os.getcwd()

print("\n-> Folder path [os.getcwd()]: \n"+cpath3)

# Config folder
config_folder_name = ".config"
    
config_folder_rt = os.path.join(cpath3,config_folder_name)

# Downlads folder
dynamic_dl_folder_name = f"{file_name} downloads"

dl_folder_name = ".downloads"

main_dl_folder_rt = os.path.join(cpath3,dl_folder_name)

thumbnails_dl_folder_name = ".thumbnails"
    
thumbnails_dl_folder_rt = os.path.join(main_dl_folder_rt,thumbnails_dl_folder_name)

# standard default ,default , high quality default, medium quality default,maximum resolution default

# Thumbnails Standard quality
std_default_res_thumbnails_dl_folder_name = ".standard quality default"

std_default_thumbnails_dl_folder_rt = os.path.join(thumbnails_dl_folder_rt,std_default_res_thumbnails_dl_folder_name)

# Thumbnails Medium quality
mq_default_res_thumbnails_dl_folder_name = ".medium quality default"

mq_default_thumbnails_dl_folder_rt = os.path.join(thumbnails_dl_folder_rt,mq_default_res_thumbnails_dl_folder_name)

# Thumbnails High quality
hq_default_res_thumbnails_dl_folder_name = ".high quality default"

hq_default_thumbnails_dl_folder_rt = os.path.join(thumbnails_dl_folder_rt,hq_default_res_thumbnails_dl_folder_name)

# Thumbnails Max quality
max_default_res_thumbnails_dl_folder_name = ".max quality default"

max_default_thumbnails_dl_folder_rt = os.path.join(thumbnails_dl_folder_rt,max_default_res_thumbnails_dl_folder_name)

# Thumbnails Default quality
default_thumbnails_dl_folder_name = ".default quality"

default_thumbnails_dl_folder_rt = os.path.join(thumbnails_dl_folder_rt,default_thumbnails_dl_folder_name)

# Audio video file
av_folder_name = ".AV files"

# av_files_dl_folder_rt = os.path.join(main_dl_folder_rt,av_folder_name)

# Directory\folder list 
dir_lsts = [config_folder_rt,main_dl_folder_rt,thumbnails_dl_folder_rt,
std_default_thumbnails_dl_folder_rt,mq_default_thumbnails_dl_folder_rt,hq_default_thumbnails_dl_folder_rt,
max_default_thumbnails_dl_folder_rt,
default_thumbnails_dl_folder_rt]

# Alternate links json file infos
links_json_name = "YT-Alt_links097Var(E)"

links_json_file = "{}.json".format(links_json_name)

vid_links_json_dic_key = "vids_links"

ch_links_json_dic_key = "ch_links"

links_jsonfl_path=os.path.join(config_folder_rt,links_json_file)

# Resolution config file infos
vid_quality_json_name = "video_quality097"

vid_quality_json_file = "{}.json".format(vid_quality_json_name)

vid_res_json_dic_key = "resolution"

default_vid_res_json_dic_value = "720p"

vid_quality_jsonfl_path=os.path.join(config_folder_rt,vid_quality_json_file)
 
# Invidous video links
invid_vid_url_lists = ['https://invidious.snopyta.org/watch?v=','https://yewtu.be/watch?v=',
'https://vid.puffyan.us/watch?v=','https://invidious-us.kavin.rocks/watch?v=',
'https://inv.riverside.rocks/watch?v=','https://invidious.namazso.eu/watch?v=',
'https://invidious.namazso.eu/watch?v=','https://inv.cthd.icu/watch?v=',

'https://invidio.xamh.de/watch?v=','https://invidious.mutahar.rocks/watch?v=',

'https://youtube.076.ne.jp/watch?v=','https://vid.mint.lgbt/watch?v=',

'https://invidious.osi.kr/watch?v=','https://yt.artemislena.eu/watch?v=',

'https://invidious.kavin.rocks/watch?v=']

# Invdous channel links
invid_ch_url_lists = ['https://invidious.snopyta.org/channel/','https://yewtu.be/channel/',
'https://vid.puffyan.us/channel/','https://invidious-us.kavin.rocks/channel/',
'https://inv.riverside.rocks/channel/','https://invidious.namazso.eu/channel/',
'https://invidious.namazso.eu/channel/','https://inv.cthd.icu/channel/',

'https://invidio.xamh.de/channel/','https://invidious.mutahar.rocks/channel/',

'https://youtube.076.ne.jp/channel/','https://vid.mint.lgbt/channel/',

'https://invidious.osi.kr/channel/','https://yt.artemislena.eu/channel/',

'https://invidious.kavin.rocks/channel/']

''' Nxt-2-Nxt activity '''
def delay(float):

    time.sleep(float)# time delay seconnds for each sequence or activities

def wipeout(var):

    time.sleep(var)

    os.system('cls')

def dirmake_2B(path_lsts):

    for path in path_lsts:

        try:
            os.makedirs(path)
        except OSError:
            pass

def save_json(jsonfl_path1,info1):
    if os.path.exists(jsonfl_path1) == False:
        with open(jsonfl_path1, "w") as jsonfl_w1:
            json.dump(info1, jsonfl_w1)

        if links_json_name in jsonfl_path1:
            print("\n-> Links data saved.")
        else:
            print("\n-> Resolution data saved.")
    else:
        pass

def read_json(jsonfl_path2,key2):
    with open(jsonfl_path2, "r") as jsonfl_r2:
        data = jsonfl_r2.read()

        json_feteched_data = json.loads(data)[key2]

    return json_feteched_data


def override_json(jsonfl_path3,info3):
    with open(jsonfl_path3, "w") as jsonfl_w3:
        json.dump(info3, jsonfl_w3)

    print(f"\n-> !!!! '{str(os.path.basename(jsonfl_path3))}' json file reseted !!!!")
 
def yt_datas():

    link_alt_yt ={vid_links_json_dic_key : invid_vid_url_lists,
                  ch_links_json_dic_key:invid_ch_url_lists}
                  
    save_json(jsonfl_path1=links_jsonfl_path,info1=link_alt_yt)

    yt_vid_res ={vid_res_json_dic_key : default_vid_res_json_dic_value}

    save_json(jsonfl_path1=vid_quality_jsonfl_path,info1=yt_vid_res)
   
    a = 0 
    #if a==0 :

    while True:

        try:

            json_vids_link_lists = read_json(jsonfl_path2=links_jsonfl_path,key2=vid_links_json_dic_key)

            json_ch_link_lists =  read_json(jsonfl_path2=links_jsonfl_path,key2=ch_links_json_dic_key)

            json_res =  read_json(jsonfl_path2=vid_quality_jsonfl_path,key2=vid_res_json_dic_key)
            
            url = input("\n_> Enter the URL of the video : \n>> ")

            if url != "":
                if "youtube" in url or "youtu.be" in url:

                    url = url.replace("youtu.be","www.youtube.com/watch?v=")

                    if "watch?v=" in url:

                        video = YouTube(url)  

                        delay(0.18)

                        try:

                            yt_video_id = video.video_id

                            print(f"\n_> Youtube video ID: {yt_video_id}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (views) , cause: \n{str(yt_gen_err)}")

                        delay(0.18)

                        try:

                            yt_video_name = video.title

                            print(f"\n_> YouTube video name:\n {yt_video_name}") 

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (title) , cause: \n{str(yt_gen_err)}")

                        delay(0.18)

                        try:
                            yt_video_desc = video.description

                            print(f"\n_> YouTube video descrpition:\n {yt_video_desc}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (description) , cause: \n{str(yt_gen_err)}")  

                        delay(0.18)

                        try:
                            yt_video_length = video.length
                            print(f"\n_> YouTube video length:\n {str(yt_video_length)}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (views) , cause: \n{str(yt_gen_err)}")

                        try:
                            
                            yt_video_published_year = video.publish_date.year

                            print(f"\n_> YouTube video published year:\n {str(yt_video_published_year)}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (published_year) , cause: \n{str(yt_gen_err)}")


                        delay(0.18)

                        try:

                            yt_video_published_date = video.publish_date.date().strftime('%d-%m-%Y')

                            print(f"\n_> YouTube video publish date:\n {yt_video_published_date}") 

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (publish_date) , cause: \n{str(yt_gen_err)}")


                        delay(0.18)

                        try:

                            yt_video_author= video.author

                            print(f"\n_> YouTube video author:\n {yt_video_author}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (author) , cause: \n{str(yt_gen_err)}")

                        yt_video_thumbnail_url = video.thumbnail_url

                        yt_video_default_thumbnail_url = f"https://img.youtube.com/vi/{yt_video_id}/default.jpg"

                        yt_video_hqdefault_thumbnail_url = f"https://img.youtube.com/vi/{yt_video_id}/hqdefault.jpg"

                        yt_video_mqdefault_thumbnail_url = f"https://img.youtube.com/vi/{yt_video_id}/mqdefault.jpg"

                        yt_video_maxresdefault_thumbnail_url = f"https://img.youtube.com/vi/{yt_video_id}/maxresdefault.jpg"

                        delay(0.18)
                        
                        try:
                                
                            yt_video_rating = video.rating


                            print(f"\n_> YouTube video rating:\n {str(yt_video_rating)}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (views) , cause: \n{str(yt_gen_err)}")

                        delay(0.18)

                        try:

                            yt_video_views = video.views

                            print(f"\n_> YouTube video views:\n {str(yt_video_views)}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (views) , cause: \n{str(yt_gen_err)}")
                            # pass

                        # vfl_720p_flsize = video.streams.filter(res='720p').filesize

                        # vfl_360p_flsize = video.streams.filter(res='360p').filesize

                        # print(f"\n_> Video size in 720p: {str(vfl_720p_flsize)}")

                        # print(f"\n_> Video size in 720p: {str(vfl_720p_flsize)}")      


                        delay(0.18)

                        try:

                            for stream in video.streams:
                                print(stream.mime_type, " ->", format(stream.filesize/(1024*1024),'.2f'), "MB")
    
                        except Exception as yt_gen_err:
                            print(f"Pytube library (stream) error , cause: \n{str(yt_gen_err)}")
                            # pass

                        try:
                            # res = "720p"
                            yt_video_file_size = format(video.streams.get_by_resolution(json_res).filesize/(1024*1024),'.2f')

                            print(f"\n_> YouTube video file sizes (for resolution: {json_res}):\n {yt_video_file_size}")

                        except Exception as yt_gen_err:
                            print(f"Pytube library error (stream) for res {json_res} , cause: \n{str(yt_gen_err)}")
                            # pass

                        delay(0.18)                

                        yt_age_restricted = video.age_restricted

                        if yt_age_restricted == True:
                            print("\n-> Age restricted...\n")

                        else:
                            print("\n-> Non-Age restricted... \n") 

                        delay(0.18)

                        print(f"\n_> YouTube video thumbnail url (standard default): {yt_video_thumbnail_url}")

                        print(f"\n_> YouTube video thumbnail url (default): {yt_video_default_thumbnail_url}")

                        print(f"\n_> YouTube video thumbnail url (high quality default): {yt_video_hqdefault_thumbnail_url}")

                        print(f"\n_> YouTube video thumbnail url (medium quality default): {yt_video_mqdefault_thumbnail_url}")

                        print(f"\n_> YouTube video thumbnail url (maximum resolution default): {yt_video_maxresdefault_thumbnail_url}")

                        # Thumbnail standard size
                        thumbnail_pic_file_name_sddefault = 'id={}(thumbnail_res_type=sddefault).jpg'.format(yt_video_id)

                        thumbnail_pic_full_path_sddefault = os.path.join(std_default_thumbnails_dl_folder_rt,thumbnail_pic_file_name_sddefault)

                        # Thumbnail default size
                        thumbnail_pic_file_name_default = 'id={}(thumbnail_res_type=default).jpg'.format(yt_video_id)

                        thumbnail_pic_full_path_default = os.path.join(default_thumbnails_dl_folder_rt,thumbnail_pic_file_name_default)

                        # Thumbnail high quality default size
                        thumbnail_pic_file_name_hqdefault = 'id={}(thumbnail_res_type=hqdefault).jpg'.format(yt_video_id)

                        thumbnail_pic_full_path_hqdefault = os.path.join(hq_default_thumbnails_dl_folder_rt,thumbnail_pic_file_name_hqdefault)

                        # Thumbnail medium quality default size
                        thumbnail_pic_file_name_mqdefault = 'id={}(thumbnail_res_type=mqdefault).jpg'.format(yt_video_id)

                        thumbnail_pic_full_path_mqdefault = os.path.join(mq_default_thumbnails_dl_folder_rt,thumbnail_pic_file_name_mqdefault)

                        # Thumbnail maximum quality default size
                        thumbnail_pic_file_name_maxresdefault = 'id={}(thumbnail_res_type=maxresdefault).jpg'.format(yt_video_id)

                        thumbnail_pic_full_path_thumbnail_pic_file_name_maxresdefault = os.path.join(max_default_thumbnails_dl_folder_rt,thumbnail_pic_file_name_maxresdefault)

                        thumbnail_paths = [thumbnail_pic_full_path_sddefault,thumbnail_pic_full_path_default,thumbnail_pic_full_path_hqdefault,thumbnail_pic_full_path_mqdefault,thumbnail_pic_full_path_thumbnail_pic_file_name_maxresdefault]
                        
                        thumbnail_urls = [yt_video_thumbnail_url, yt_video_default_thumbnail_url, yt_video_hqdefault_thumbnail_url, yt_video_mqdefault_thumbnail_url, yt_video_maxresdefault_thumbnail_url]
                        
                        for i in range(0,len(thumbnail_paths),1):
                            try:
                                if os.path.exists(thumbnail_paths[i])==False:
                                    
                                    img_file = open(thumbnail_paths[i], "wb")

                                    img_file.write(requests.get(thumbnail_urls[i]).content)

                                    img_file.close()

                                    print(f"\n-> '{os.path.basename(thumbnail_paths[i])}' thumbnail saved.")                                   
                                else:

                                    print(f"\n-> '{os.path.basename(thumbnail_paths[i])}' thumbnail already exists.")
 
                            except Exception as generic_req_err:

                                print(f"\n->Generic Error (url:{thumbnail_urls[i]}): {generic_req_err}")

               

                        delay(0.18) 

                        # yt_stream = video.streams.

                        # yt_stream.d

                        try:
                            # res2 = "720p"
                            yt_stream = video.streams.filter(res=json_res).first()

                            # yt_stream.download(av_files_dl_folder_rt)

                            print(f"\n-> Video saved.")
                        
                        except Exception as yt_gen_err:
                            print(f"Pytube library error (video download filter) for res {json_res} , cause: \n{str(yt_gen_err)}")
                            # pas
                        
                        try:
                            yt_aud_stream = video.streams.get_audio_only()
                            # yt_aud_stream.download(av_files_dl_folder_rt)

                            print("\n-> Audio saved.")
                        
                        except Exception as yt_gen_err:
                            print(f"Pytube library error (audio download - get_audio_only) , cause: \n{str(yt_gen_err)}")

                        print("\n-> Alternative video links: ")

                        for n in range(0, len(json_vids_link_lists),1):
                            print(f"\n_> Alternative link {str(n+1)}:- {json_vids_link_lists[n]}{video.video_id}")
                        break                

                    elif "channel" in url:

                        channel = Channel(url)

                        print(f'YouTube channel name: {channel.channel_name}')
                        
                        yt_ch_url_split = url.split('channel/')

                        print("\n_> Youtube channel ID: "+yt_ch_url_split[1])

                        print("Alternative channel links: ")

                        for n in range(0, len(json_ch_link_lists), 1):

                            print(f"\nAlternative link {str(n+1)}:- {json_ch_link_lists[n]}{yt_ch_url_split[1]}")

                        break
        
                    elif "user" in url:

                        channel = Channel(url)

                        print(f'YouTube Channel name: {channel.channel_name}')               

                        yt_ch_url_split = url.split('user/')

                        print("\n_> Youtube channel ID: "+yt_ch_url_split[1])

                        print("Alternative channel links: ")

                        for n in range(0, len(json_ch_link_lists), 1):

                            print(f"\nAlternative link {str(n+1)}:- {json_ch_link_lists[n]}{yt_ch_url_split[1]}")

                        break
        
                    elif "playlist" in url: 

                        yt_playlist_infos = Playlist(url)

                        yt_playlist_infos._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

                        delay(0.18)

                        try:
                            playlist_title1 = yt_playlist_infos.title
                            playlist_title_re1 = playlist_title1.replace("'","").replace(":","").replace("'","").replace("|","").replace("/","").replace("\\","").replace("<","").replace(">","").replace("*","").replace("?","")

                            print(f"\n_> Playlist title: \n{playlist_title1}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_tiltle) , cause: \n{str(yt_playlist_gen_err)}")

                        """
                        try:
                            playlist_title2 = yt_playlist_infos.title
                            playlist_title_re2 = playlist_title2.replace("'"," ").replace(":"," ").replace("'"," ").replace("|"," ").replace("/"," ").replace("\\"," ").replace("<"," ").replace(">"," ").replace("*"," ").replace("?"," ")

                            # print(f"\n_> Playlist title: \n{playlist_title2}")

                            # delay(0.18)
                            
                            pass
                        except:
                            pass

                        """

                        try:
                            playlist_title_sub_folder = os.path.join(cpath3,playlist_title1)

                            os.makedirs(playlist_title_sub_folder)
                                        
                        except OSError:
                            pass

                        try:
                            
                            playlist_title_sub_folder_re1 = os.path.join(cpath3,playlist_title_re1)

                            os.makedirs(playlist_title_sub_folder_re1)
                                        
                        except OSError:
                            pass

                        try:
                            print(f"\n-> Folder '{playlist_title1}' (Orginal for folder creation - No Modiied) status: {os.path.exists(playlist_title_sub_folder)}")   
                                
                            print(f"\n-> Folder '{playlist_title_re1}' (Refined for folder creation - 1st modification) status: {os.path.exists(playlist_title_sub_folder_re1)}")

                        except:
                            pass

                        delay(0.18)
                        
                        try:
                            playlist_owner = yt_playlist_infos.owner

                            print(f"\n_> Playlist owner: \n{playlist_owner}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_owner) , cause: \n{str(yt_playlist_gen_err)}")

                        
                        delay(0.18)
                        
                        try:
                            playlist_owner_id = yt_playlist_infos.owner_id

                            print(f"\n_> Playlist owner ID: \n{playlist_owner_id}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_owner_id) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)
                        
                        try:
                            playlist_owner_url = yt_playlist_infos.owner_url
                        
                            print(f"\n_> Playlist owner url: \n{playlist_owner_url}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_owner_url) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)
                        
                        try:
                            playlist_url = yt_playlist_infos.playlist_url
                        
                            print(f"\n_> Playlist url: \n{playlist_url}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_url) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_id = yt_playlist_infos.playlist_id
                            
                            print(f"\n_> Playlist ID: \n{playlist_id}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_id) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_views = yt_playlist_infos.views
                            
                            print(f"\n_> Playlist views: \n{playlist_views}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_views) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_api_key = yt_playlist_infos.yt_api_key
                        
                            print(f"\n_> Playlist API key: \n{playlist_api_key}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_api_key) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_description = yt_playlist_infos.description
                            
                            print(f"\n_> Playlist description: \n{playlist_description}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist description) , cause: \n{str(yt_playlist_gen_err)}")

                        try:
                            print(f"\n-> Videos in playlist '{playlist_title1}': \n")
                            urls_lists_playlist = yt_playlist_infos.video_urls

                            for n in range(0,len(urls_lists_playlist),1):
                                
                                playlist_yt = YouTube(urls_lists_playlist[n])
                                playlist_yt_video_name =  playlist_yt.title
                                playlist_yt_video_url = playlist_yt.watch_url
                                playlist_yt_video_id = playlist_yt.video_id

                                print("\t\n----------------------------------------------------------------------------")
                
                                print(f"_>\t\n ({str(n+1)}) - Video name : {playlist_yt_video_name} | Video url : {playlist_yt_video_url} .")

                                print("\n-> Alternative video links: ")

                                for n in range(0, len(json_vids_link_lists,1)):

                                    print("\t\n\t.............................................................................")

                                    print(f"_> \t\n\tAlternative link {str(n+1)}:- {json_vids_link_lists[n]}{playlist_yt_video_id}")

                                    print("\t\n\t.............................................................................")

                                    delay(0.18)

                                print("\t\n-----------------------------------------------------------------------------")

                                delay(0.18)
                                
                            delay(0.18)
                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_videos_title: [{playlist_title1}]) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)
                        
                        try:

                            playlist_html = yt_playlist_infos.html
                        
                            print(f"\n_> Playlist html: \n{playlist_html}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_html) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_videos = yt_playlist_infos.videos
                            
                            print(f"\n_> Playlist videos: \n{playlist_videos}")
                        
                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_videos) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_sidebar_info = yt_playlist_infos.sidebar_info
                        
                            print(f"\n_> Playlist side bar info: \n{playlist_sidebar_info}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (sidebar_info) , cause: \n{str(yt_playlist_gen_err)}")

                        delay(0.18)

                        try:
                            playlist_config = yt_playlist_infos.ytcfg
                        
                            print(f"\n_> Playlist config: \n{playlist_config}")

                        except Exception as yt_playlist_gen_err:
                            print(f"Pytube library error (playlist_config [ytcfg]) , cause: \n{str(yt_playlist_gen_err)}")   

                        # pass

                        break
                    else:
                        pass
                elif "invidious" in url:

                    if "watch?v=" in url:
                        invid_vid_url_split = url.split('watch?v=')

                        print("Alternative links to video links: ")

                        print(f"\n_> Invidious video ID: {invid_vid_url_split[1]}")

                        for n in range(0, len(json_vids_link_lists), 1):

                            print(f"\n_> Alternative link {str(n)}:- {json_vids_link_lists[n]}{invid_vid_url_split[1]}")

                        break                       

                    elif "channel" in url:
                        invid_ch_url_split = url.split('channel/')

                        print("\n_> Invidious channel ID: "+invid_ch_url_split[1])

                        print("\nAlternative channel links: ")

                        for n in range(0, len(json_ch_link_lists), 1):

                            print(f"\n_> Alternative link {str(n+1)}:- {json_ch_link_lists[n]}{invid_ch_url_split[1]}")

                        break

                    else:
                        pass                

                elif "youtube" not in url or "invidious" not in url:
                    for n in range(0, len(json_vids_link_lists),1):
                        print(f"\n_> Alternative link {str(n+1)}:- {json_vids_link_lists[n]}{url}")
                    break
                
                else:
                    pass
            else:
                print("\n>> Empty values are invalid.")    

            # break
       
        except json.decoder.JSONDecodeError as json_err:

            print(f"\n-> Yt saver json file error , cause: \n{str(json_err)}")

            delay(0.21)

            break
            
        except KeyError as key_err:

            print(f"\n-> Yt saver key error , cause: \n{str(key_err)}")

            if (vid_links_json_dic_key in str(key_err) or ch_links_json_dic_key in str(key_err)):
                override_json(jsonfl_path3=links_jsonfl_path,info3=link_alt_yt)                
            else:               
                override_json(jsonfl_path3=vid_quality_jsonfl_path,info3=yt_vid_res)  
                
            # break

            delay(0.21) 
        
        except Exception as err:

            print(f"\n-> Yt saver error , cause: \n{str(err)}")

            delay(0.21)

            break
  
        # break
if __name__=='__main__':

    dirmake_2B(path_lsts=dir_lsts)

    yt_datas()

    while True:
        print("\nDo you wish to  use the app again?")

        opts = input("\nY or N >> ").lower()

        #wipeout(0.12)

        if "y" == opts:

            wipeout(0.12)

            print("\n<___________________________________________________>")

            yt_datas()
            
        elif "n" == opts:
            #sys.exit()
            break
        else:
            print("Option invalid.")

            wipeout(2.83)
