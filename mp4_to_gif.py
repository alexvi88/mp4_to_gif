import os
from moviepy.editor import VideoFileClip
from settings import directory_with_mp4, directory_for_gif


videos = [file_name for file_name in os.listdir(directory_with_mp4)
          if os.path.splitext(file_name)[1] == ".mp4"]

for video_name in videos:
    try:
        video_path = directory_with_mp4 + '/' + video_name
        cur_clip = VideoFileClip(video_path)
        cur_gif_path = directory_for_gif + '/' + video_name.replace('.mp4', '.gif')
        cur_clip.write_gif(cur_gif_path)
        os.remove(video_path)
    except Exception as e:
        print(e)
