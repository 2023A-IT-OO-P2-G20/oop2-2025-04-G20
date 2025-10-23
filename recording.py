import ffmpeg
import os


def record(duration: int = 10, output_file: str = "python-audio-output.wav", device: str = ":0", fmt: str = "avfoundation") -> str:
    """Record audio using ffmpeg and save to output_file.

    Args:
        duration: seconds to record
        output_file: wav path to write
        device: input device identifier (default ":0" for macOS avfoundation)
        fmt: ffmpeg input format (e.g., 'avfoundation', 'alsa', 'dshow')

    Returns:
        Absolute path to the saved WAV file.
    """
    try:
        print(f"{duration}秒、マイクからの録音を開始します...")
        (
            ffmpeg
            .input(device, format=fmt, t=duration)
            .output(output_file, acodec="pcm_s16le", ar="44100", ac=1)
            .run(overwrite_output=True)
        )
        abs_path = os.path.abspath(output_file)
        print(f"録音が完了しました。{abs_path} に保存されました。")
        return abs_path

    except ffmpeg.Error as e:
        err = e.stderr.decode() if hasattr(e, "stderr") and e.stderr else str(e)
        print(f"エラーが発生しました: {err}")
        raise
    except Exception:
        raise
import ffmpeg
import time

# 録音時間（秒）
duration = 10
# 出力ファイル名
output_file = 'python-audio-output.wav'

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")
    # FFmpegコマンドを実行
    # -f <デバイス入力形式>: OSに応じたデバイス入力形式を指定
    #   - Windows: 'dshow' または 'gdigrab'
    #   - macOS: 'avfoundation'
    #   - Linux: 'alsa'
    # -i <入力デバイス名>: デバイス名を指定
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration) # macOSの例
        .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
        .run(overwrite_output=True)
    )
    print(f"録音が完了しました。{output_file}に保存されました。")

except ffmpeg.Error as e:
    print(f"エラーが発生しました: {e.stderr.decode()}")
except Exception as e:
    print(f"予期せぬエラー: {e}")