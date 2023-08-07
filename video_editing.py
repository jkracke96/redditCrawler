from moviepy.editor import *
from audio_editing import run_audio_edit


def get_screenshots(post_folder, comment_folder):
    """
    Iterate through posts and find the respective screenshots. The add post and comment pairs to content dict
    :param post_folder
    :param comment_folder
    :return: content dict including all post and comment pairs as values with the respective post as key
    """
    content = dict()
    # Iterate through posts and find the respective screenshots. The add post and comment pairs to content dict
    for filename in os.listdir(post_folder):
        current_post = []
        if filename.endswith(".png"):
            current_post.append(f"{post_folder}/{filename}")
            post_nr = filename.replace(".png", "_")
            comment_filenames = os.listdir(comment_folder)
            comment_filenames.sort()
            for comment_filename in comment_filenames:
                if post_nr in comment_filename:
                    current_post.append(f"{comment_folder}/{comment_filename}")
        if len(current_post) > 0:
            content[filename] = current_post
    return content


def determine_audio_clip_lenght(post):
    durations = []
    for file in post:
        audio_file = file.replace("screenshots/posts", "audio")
        audio_file = audio_file.replace("screenshots/comments", "audio")
        audio_file = audio_file.replace(".png", ".mp3")
        try:
            audio_clip = AudioFileClip(audio_file)
            durations.append(audio_clip.duration)
        except Exception as e:
            print("mp3 file not found \n", e)
            durations.append(0)
    return durations


def create_video(content, video_output_folder):
    pause = 1
    for key in content.keys():
        post = content[key]
        durations = determine_audio_clip_lenght(post)
        clips = [ImageClip(p).set_duration(durations[post.index(p)]+pause) for p in post]

        video_name = key.replace(".png", "")
        concat_clip = concatenate_videoclips(clips, method="compose")

        run_audio_edit(video_name, "combined_audio.mp3", pause)
        audio_file_clip = AudioFileClip("combined_audio.mp3")
        concat_clip = concat_clip.set_audio(audio_file_clip)

        concat_clip.write_videofile(
            f"{video_output_folder}/{video_name}.mp4",
            codec="libx264",
            audio_codec="aac",
            fps=24
        )


if __name__ == "__main__":
    # set params
    post_folder = "screenshots/posts"
    comment_folder = "screenshots/comments"
    video_output_folder = "video"

    content = get_screenshots(post_folder, comment_folder)
    create_video(content, video_output_folder)
