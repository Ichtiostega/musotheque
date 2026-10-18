import ffmpeg
from pathlib import Path
from argparse import ArgumentParser

def subparser(parser: ArgumentParser):
    def target_validation(target: str) -> Path:
        target = Path(target)
        if not target.exists():
            raise ValueError("The target doesn't exist")
        return target
    parser.add_argument("-t", "--target", type=target_validation)


def confirmation_prompt(files_to_change: list[Path]) -> bool:
    for file in files_to_change:
        print(file)
    yn = input("The above files will be transcoded. Proceed? [y/N]")
    return yn.lower() == 'y'

    
def flac2mp3(path: Path):
    flac_files = list(path.glob('**/*.flac')) if path.is_dir() else [path]
    if confirmation_prompt(flac_files):
        for fname in flac_files:
            new_fname = fname.with_suffix('.mp3')
            ffmpeg.input(fname).output(str(new_fname), audio_bitrate="320k").run()
            fname.unlink()

if __name__ == "__main__":
    parser = ArgumentParser(description="flac to mp3 transcoder")
    parser.add_argument("-t", "--target", type=Path, help="path to the file/directory to be transcoded")
    args = parser.parse_args()
    flac2mp3(args.target)