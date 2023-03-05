import argparse
from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=None)
def count_unique_chars(s):
    return Counter(Counter(s).values())[1]


def process_string(s):
    print(count_unique_chars(s))
    

def process_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(count_unique_chars(line.strip()))


def main(args):
    if args.string:
        process_string(args.string)
    elif args.file:
        process_file(args.file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Подсчитайте количество уникальных символов в строке или файле')
    parser.add_argument('--string', help='Входная строка')
    parser.add_argument('--file', help='Входной файл')
    args = parser.parse_args()
    main(args)