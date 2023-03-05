import argparse
from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=None)
def count_unique_chars(s):
    return Counter(Counter(s).values())[1]


def process_string(s):
    return count_unique_chars(s)
    

def process_file(file_arg):
    results = []
    with file_arg as f:
        for line in f:
            results.append(count_unique_chars(line.strip()))
    return results

def create_parser(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', help='Входная строка')
    parser.add_argument('--file', type=argparse.FileType('r'), help='Входной файл')
    return parser

def main(argv):
    argv = create_parser(args)
    if args.string:
        process_string(args.string)
    elif args.file:
        process_file(args.file)

if __name__ == '__main__':
    print(main())
