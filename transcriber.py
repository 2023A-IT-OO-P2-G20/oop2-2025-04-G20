import mlx_whisper
from pydub import AudioSegment
import numpy as np
import os
from typing import Optional


# ローカルのwhisper-base-mlxディレクトリのパスを取得
DEFAULT_MODEL_PATH = os.path.join(os.path.dirname(__file__), "whisper-base-mlx")


def preprocess_audio_segment(sound: AudioSegment) -> AudioSegment:
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound


def transcribe_file(path: str, model_path: Optional[str] = None) -> str:
    """Transcribe an audio file using mlx_whisper.

    Returns the transcription string.
    """
    model = model_path or DEFAULT_MODEL_PATH
    return mlx_whisper.transcribe(path, path_or_hf_repo=model)


def transcribe_audiosegment(sound: AudioSegment, model_path: Optional[str] = None) -> str:
    sound = preprocess_audio_segment(sound)
    arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
    model = model_path or DEFAULT_MODEL_PATH
    return mlx_whisper.transcribe(arr, path_or_hf_repo=model)