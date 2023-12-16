import argparse

from file_utils import concatenate_files


def process_arguments(args):
    concatenated_files = concatenate_files(args.path, args.exclude)
    print(concatenated_files)


def main(args=None):
    parser = argparse.ArgumentParser(description="Example script.sh that accepts command-line arguments.")
    parser.add_argument('path', help='Directory path to process')
    parser.add_argument('-e', '--exclude', nargs='*', help='List of files to exclude', default=None)
    args = parser.parse_args(args)
    return process_arguments(args)


if __name__ == "__main__":
    print(main())
