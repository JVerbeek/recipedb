import os
import argparse


def argument_handler():
    """
    Handles command line arguments.
    :return: argparse namespace object
    """
    parser = argparse.ArgumentParser(description="enter description")
    parser.add_argument("file_path", help="path to the file you want to print")
    parser.add_argument("-printer", "-p", help="name of desired printer",
                        default = "HP_DeskJet_2600_series_E0A01B_")
    args = parser.parse_args()
    return args


def print_file(file_path: str, printer: str) -> None:
    """
    Prints a file from specified printer.
    :param file_path: path to the file that needs to be printed
    :type file_path: str
    :param printer: name of the printer
    :type printer: str
    """
    os.system(f"lpr -P {printer} {file_path}")


def main(args):
    """
    Calls print function with a file path.
    :param args: argparse namespace object
    """
    print_file(os.path.abspath(args.file_path), args.printer)


if __name__ == "__main__":
    arguments = argument_handler()
    main(arguments)
