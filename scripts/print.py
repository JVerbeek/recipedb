import os
import argparse


def argument_handler():
    parser = argparse.ArgumentParser(description="enter description")
    parser.add_argument("file_path", help="path to the file you want to print")
    args = parser.parse_args()
    return args


def print_file(file_path):
    os.system(f"lpr -P HP_DeskJet_2600_series_E0A01B_ {file_path}")


def main(args):
    print_file(os.path.abspath(args.file_path))


if __name__ == "__main__":
    arguments = argument_handler()
    main(arguments)
