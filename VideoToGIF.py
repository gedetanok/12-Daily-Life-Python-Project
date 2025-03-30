
from moviepy.editor import VideoFileClip

def convert_video_to_gif(video_path, gif_path, start_time=0, duration=None):
    # Load video clip
    clip = VideoFileClip(video_path)
    
    # Duration for GIF, if not specified use whole video
    if duration:
        clip = clip.subclip(start_time, start_time + duration)
    else:
        clip = clip.subclip(start_time, clip.duration)
    
    # Write the clipped video as GIF
    clip.write_gif(gif_path)
    print(f"GIF saved to {gif_path}")

video_path = "Sample_Video.mp4"  # Path to your video file
gif_path = "output.gif"  # Path where the gif will be saved
convert_video_to_gif(video_path, gif_path, start_time=0, duration=15)