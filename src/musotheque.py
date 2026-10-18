from transcoders import flac2mp3
from constants import Operations
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(description="music library organization utility")
subparsers = parser.add_subparsers(title="operations", dest="operation")
transcode_parser = subparsers.add_parser("transcode")
flac2mp3.subparser(transcode_parser)
args = parser.parse_args()

match(args.operation):
    case "transcode":
        flac2mp3.flac2mp3(args.target)