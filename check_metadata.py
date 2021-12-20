import argparse

def check_metadata(content, field_list, filename):
    
    checklist = {}
    for line in content:
        if line.startswith("#"):
            for field in field_list:
                if field in line:
                    checklist[field] = True
                    
    if len(field_list) != len(checklist):
        return 1
            
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--fields', type=int, default=None,
        help='List of metadata fields to check.',
    )
    args = parser.parse_args(argv)
    
    if args.fields is not None:
        field_list = fields.split(",")
    else:
        return 0

    retv = 0

    for filename in args.filenames:
        with open(filename, 'r') as f:
            content = f.readlines()
        retv |= check_metadata(content, field_list, filename)

    return retv
