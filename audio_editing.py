from pydub import AudioSegment
import os


def adjust_audio_speed(audio_segment, target_duration):
    target_duration_ms = target_duration * 1000
    speed_factor = len(audio_segment) / target_duration_ms

    adjusted_audio = audio_segment.set_frame_rate(int(audio_segment.frame_rate / speed_factor))

    return adjusted_audio


def concatenate_audio(audio_path, audio_files, output_filename, target_duration=5):
    combined_audio = AudioSegment.silent(duration=0)

    for file in audio_files:
        print(f"{audio_path}/{file}")
        audio_segment = AudioSegment.from_file(f"{audio_path}/{file}")


        # Adjust the speed to match the target duration
        adjusted_audio = adjust_audio_speed(audio_segment, target_duration)

        combined_audio += adjusted_audio

    combined_audio.export(output_filename, format="mp3")


if __name__ == "__main__":
    # List of audio files to concatenate
    audio_path = "audio"
    audio_files = os.listdir(audio_path)
    audio_files.remove("__init__.py")
    audio_files.sort()

    # Output filename for the concatenated audio
    output_filename = f"combined_audio.mp3"

    # Call the concatenate_audio function
    concatenate_audio(audio_path, audio_files, output_filename)
