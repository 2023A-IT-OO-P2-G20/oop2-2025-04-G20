
import argparse
import sys
from recording import record
from transcriber import transcribe_file
from haba_woker3 import save_text


def main(argv=None):
	argv = argv or sys.argv[1:]
	p = argparse.ArgumentParser(description="録音→文字起こしパイプライン CLI")
	sub = p.add_subparsers(dest="cmd")

	r = sub.add_parser("record", help="マイクから録音して WAV を作る")
	r.add_argument("-d", "--duration", type=int, default=10, help="録音秒数")
	r.add_argument("-o", "--output", default="python-audio-output.wav", help="出力ファイル")

	t = sub.add_parser("transcribe", help="ファイルを文字起こしする")
	t.add_argument("file", help="入力オーディオファイルパス")

	s = sub.add_parser("save", help="文字列を保存する（ファイルへ）")
	s.add_argument("text", help="保存するテキスト")
	s.add_argument("-d", "--dir", default="transcriptions", help="保存先ディレクトリ")

	run = sub.add_parser("run", help="record -> transcribe -> save を順に実行する")
	run.add_argument("-d", "--duration", type=int, default=10, help="録音秒数")
	run.add_argument("-o", "--output", default="python-audio-output.wav", help="一時出力ファイル")

	args = p.parse_args(argv)
	if args.cmd == "record":
		path = record(duration=args.duration, output_file=args.output)
		print(path)
	elif args.cmd == "transcribe":
		text = transcribe_file(args.file)
		print(text)
	elif args.cmd == "save":
		path = save_text(args.text, directory=args.dir)
		print(path)
	elif args.cmd == "run":
		wav = record(duration=args.duration, output_file=args.output)
		text = transcribe_file(wav)
		saved = save_text(text)
		print(f"Saved: {saved}")
	else:
		p.print_help()


if __name__ == "__main__":
	main()

