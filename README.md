# oop2-2025-04-G20
## リポジトリの目的
-マイクから10秒間音声を文字おこししてテキストファイルに保存するpythonプログラムをチームで、開発、共有することを目的としている。
## 使用するモジュール
- 'ffmpeg-python'
- 'mlx_whisper'
- 'pydub'
- 'numpy'
- 'os'
- 'datetime'
## 実行手順
- 04_group/
- 1,recording.py               録音用スクリプト（FFmpeg使用）
- 2,transcriber.py             Whisperを用いた文字起こし処理
- 3,saveTranscription.py       結果を自動保存
- 4,transcriptions/            出力された文字起こしテキストが保存されるフォルダ
- lecture04_main.py          メイン処理（録音→文字起こし→保存）
　
## 作成者情報
- リーダー：守長　拓真
- 作業者1：西田　詩音
- 作業者2:石丸　凛弥
- 作業者3： 幅　幸志郎
