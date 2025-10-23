# - 文字起こしされた文字列を保存する処理（上書きしない）- #
# 保存形式が他人にもわかるように，README.mdに出力例を掲載します
# 作業ブランチを作成して，リーダーにプルリクエストを承認してもらいます
# 音声ファイル名「onsei」
# 作業者1のコード名「recording.py」
# 作業者2のコード名「transcriber.py」


import os
from datetime import datetime

def save_text(text: str, directory: str = "transcriptions", base_name: str = "onsei") -> str:
    """
    文字起こし結果をファイルに保存する（上書きしない）

    Parameters
    ----------
    text : str
        保存するテキスト
    directory : str
        保存先ディレクトリ

    Returns
    -------
    str
        保存したファイルのパス
    """

    # 保存先のフォルダーがなければ作成
    os.makedirs(directory, exist_ok=True)

    # タイムスタンプで重複を防止
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_name}_{timestamp}.txt"
    filepath = os.path.join(directory, filename)

    # UTF-8でテキスト書き込み
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"文字起こし結果を {filepath} に保存しました。")
    return filepath