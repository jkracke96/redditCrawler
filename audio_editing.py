from pydub import AudioSegment
import os


def adjust_audio_speed(audio_segment, target_duration):
    target_duration_ms = target_duration * 1000
    speed_factor = len(audio_segment) / target_duration_ms

    adjusted_audio = audio_segment.set_frame_rate(int(audio_segment.frame_rate / speed_factor))

    return adjusted_audio


def concatenate_audio(audio_path, audio_files, output_filename, pause):
    combined_audio = AudioSegment.silent(duration=0)

    for file in audio_files:
        print(f"{audio_path}/{file}")
        audio_segment = AudioSegment.from_file(f"{audio_path}/{file}")
        pause_segment = AudioSegment.silent(duration=pause*1100)    # multiplied by 1000 for ms to s conversion
        print(len(audio_segment))
        audio_segment += pause_segment
        print(len(audio_segment))
        combined_audio += audio_segment

    combined_audio.export(output_filename, format="mp3")


def run_audio_edit(post, output_filename, pause=0):
    # List of audio files to concatenate
    audio_path = "audio"
    all_audio_files = os.listdir(audio_path)
    all_audio_files.remove("__init__.py")
    all_audio_files.sort()
    audio_files = []
    # without 2nd condition, e.g. post10 would also be selected when post "post1"
    for file in all_audio_files:
        if post in file:
            if "comment" not in file and len(post) + 4 == len(file):
                audio_files.append(file)
            elif f"{post}_comment" in file:
                audio_files.append(file)

    # Call the concatenate_audio function
    concatenate_audio(audio_path, audio_files, output_filename, pause)
