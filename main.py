from moviepy.editor import VideoFileClip ,TextClip ,CompositeVideoClip
import os

def split_and_resize_video(video_path, clip_duration=60,  target_width=1080, target_height=1920):
    # Load the video file
    video = VideoFileClip(video_path)

    # Calculate the total duration of the video in seconds
    total_duration = video.duration

    # Calculate the number of full clips and the duration of the last clip
    num_full_clips = int(total_duration // clip_duration)
    remaining_duration = total_duration % clip_duration

    # List to store the generated clips
    def resize_and_add_background(clip, target_width, target_height,title=""):
        # Resize the clip to the target width
        clip_resized = clip.resize(width=target_width)
        # Calculate top margin to center the video vertically
        top_margin = (target_height - clip_resized.size[1]) // 2
        # Add white background
        clip_with_background = clip_resized.on_color(
            size=(target_width, target_height),
            color=(255, 255, 255),
            pos=('center', 'center')
        )

        # Add title text
        if title:
            txt_clip = TextClip(title, fontsize=70, font='Arial-Bold', color='black', bg_color='white')
            # Add space at the top
            txt_clip = txt_clip.set_position(("center",0.2),relative=True).set_duration(clip.duration)
            # Overlay text on the video clip
            clip_with_background = CompositeVideoClip([clip_with_background, txt_clip])
        return clip_with_background

    clips = []

    # Extract full 1-minute clips
    for i in range(num_full_clips):
        start_time = i * clip_duration
        end_time = start_time + clip_duration
        clip = video.subclip(start_time, end_time)

        clip_with_background = resize_and_add_background(clip, target_width, target_height,f"Demon Slayer 2 Part {i + 1}")

        # Save each 1-minute clip
        output_path = f"output/Demon Slayer 2 Part {i + 1}.mp4"
        clip_with_background.write_videofile(output_path)
        print(f"Saved {output_path}")

        clips.append(clip_with_background)

    # Extract and save the remaining clip if any
    if remaining_duration > 0:
        start_time = num_full_clips * clip_duration
        end_time = start_time + remaining_duration
        remaining_clip = video.subclip(start_time, end_time)

        # Resize and add background
        remaining_clip_with_background = resize_and_add_background(remaining_clip, target_width, target_height,f"Demon Slayer 2 Part {i + 1}")

        # Save the remaining clip
        output_path = f"output/Demon Slayer 2 Part {num_full_clips + 1}.mp4"
        remaining_clip_with_background.write_videofile(output_path)
        print(f"Saved {output_path}")

        clips.append(remaining_clip_with_background)

    return clips


# Path to your video file
video_folder = "video"

# Process each video in the folder
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        video_path = os.path.join(video_folder, filename)
        print(f"Processing {video_path}")
        split_and_resize_video(video_path)
