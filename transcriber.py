import mlx_whisper
from pydub import AudioSegment
import numpy as np
import os

# 音声ファイルを指定して文字起こし
audio_file_path = "python-audio-output.wav"

# ローカルのwhisper-base-mlxディレクトリのパスを取得
model_path = os.path.join(os.path.dirname(__file__), "whisper-base-mlx")

result = mlx_whisper.transcribe(
  audio_file_path, path_or_hf_repo=model_path
)

print(result)

# 音声データを指定して文字起こし
def preprocess_audio(sound):
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

audio_data = []

for data in audio_data:
    sound = preprocess_audio(data)
    # Metal(GPU)が扱えるNumpy Array形式に変換
    arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
    result = mlx_whisper.transcribe(
        arr, path_or_hf_repo=model_path
    )
    print(result)