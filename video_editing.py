from moviepy.editor import *
from audio_editing import run_audio_edit
import json


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


def get_post_text(post):
    post_keys = []
    # prepare post and comment keys for json
    for file in post:
        audio_text = file.replace("screenshots/posts/", "")
        audio_text = audio_text.replace("screenshots/comments/", "")
        audio_text = audio_text.replace(".png", "")
        post_keys.append(audio_text)

    # get texts for relevant post and comments from json
    f = open("screenshots/texts.json", "r")
    json_data = json.load(f)
    texts = []
    for post_key in post_keys:
        texts.append(json_data[post_key])

    return texts


def define_subtitle_tuples(texts, durations, pause):
    # iterate through each word for each post text
    subtitles = []
    interval_start = 0
    for text in texts:
        words = text.split()
        spaces = text.count(" ")
        chars_text = len(text)
        space_length = spaces/chars_text

        # for each word, determine the relative length compared to the whole text and determine the interval for which
        # the subtitle is supposed to be shown

        # maybe use gtts to determine the exact length of every word?
        for word in words:
            chars_word = len(word)
            duration = durations[texts.index(text)]
            interval_length = (chars_word/chars_text)*duration
            if words.index(word) < len(words)-1:
                interval_end = interval_start + interval_length + space_length
                subtitles.append(((interval_start, interval_end), word))
                interval_start = interval_end
            else:
                #interval_end = interval_start + interval_length + pause
                interval_end = interval_start + interval_length
                subtitles.append(((interval_start, interval_end), word))
                interval_start = interval_end
    if interval_end > duration:
        multiplier = duration * interval_end
        adj_subtitles = [i * multiplier for i in subtitles]

    return subtitles


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

        post_texts = get_post_text(post)
        subtitles = define_subtitle_tuples(post_texts, durations, pause)

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
