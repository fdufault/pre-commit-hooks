from typing import Optional
from typing import Sequence
import argparse


def get_checklist(fields):
    checklist = {}
    for field in fields.split(","):
        checklist[field] = False
    return checklist


def check_metadata(content, fields, filename):
    status = 0
    checklist = get_checklist(fields)
    for line in content:
        if line.startswith("#"):
            for field in fields:
                if field in line:
                    checklist[field] = True
    for field in checklist:
        if not checklist[field]:
            print(filename, "missing field:", field)
            status = 1
    return status 


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--fields', default=None,
        help='List of metadata fields to check.',
    )
    args = parser.parse_args(argv)
    if args.fields is not None:
        fields = args.fields.split(",")
    else:
        return 0
    retv = 0
    for filename in args.filenames:
        with open(filename, 'r') as f:
            content = f.readlines()
        retv |= check_metadata(content, fields, filename)
    return retv
