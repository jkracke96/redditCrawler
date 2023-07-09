from moviepy.editor import *


def get_screenshots(post_folder, comment_folder):
    content = dict()
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


def create_video(content, video_output_folder):
    for key in content.keys():
        post = content[key]
        clips = [ImageClip(p).set_duration(2) for p in post]

        video_name = key.replace(".png", "")
        concat_clip = concatenate_videoclips(clips, method="compose")
        concat_clip.write_videofile(f"{video_output_folder}/{video_name}.mp4", fps=24)


if __name__ == "__main__":
    post_folder = "screenshots/posts"
    comment_folder = "screenshots/comments"
    video_output_folder = "video"

    content = get_screenshots(post_folder, comment_folder)

    create_video(content, video_output_folder)
