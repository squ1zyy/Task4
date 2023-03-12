import argparse
from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=None)
def count_unique_chars(s):
    return Counter(Counter(s).values())[1]


# def process_file(file_arg):
#     results = []
#     with file_arg as f:
#         for line in f:
#             results.append(count_unique_chars(line.strip()))
#     return results


def create_parser(string):
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', help='Входная строка')
    parser.add_argument('--file', type=argparse.FileType('r'), help='Входной файл')
    return parser.parse_args(string)


def main(argv=None):
    args = create_parser(argv)

    if args.file:
        with args.file as file:
            return count_unique_chars(file.read())
    elif args.string:
        return count_unique_chars(args.string)
    return 'Введите команду --string/--file: '

if __name__ == '__main__':
    print(main('--string', 'abbbccdf'))