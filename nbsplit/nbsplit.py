#!/usr/bin/env python3
# Andreas Herten, 8 March 2019; MIT License
import json
import copy
import os
import sys
import argparse
import textwrap
import logging

logger = logging.getLogger(__file__)


def parse(inputfile, keep, remove, basekey):
    """
    From inputfile, parse the JSON and remove those cells which have values of the basekey, which are in the list of tags to remove but not in the list of tags to remove.
    """
    notebook = json.load(inputfile)

    if not isinstance(keep, list): keep = [keep]
    if not isinstance(remove, list): remove = [remove]

    notebook_new = copy.deepcopy(notebook)
    notebook_new["cells"] = []

    for cell in notebook["cells"]:
        keepcell = True
        for key in remove:
            cell_tags = None
            if basekey in cell["metadata"]:
                cell_tags = cell["metadata"][basekey]
                if isinstance(cell_tags, str): cell_tags = [cell_tags]
            if cell_tags == None:
                if key == "all":
                    keepcell = False
            if cell_tags != None:
                if key in cell_tags or key == "all":
                    for tag in cell_tags:
                        if tag not in keep:
                            keepcell = False
        if keepcell == True:
            notebook_new["cells"].append(cell)
        else:
            logger.info("Removing cell with JSON content:\n{}".format(json.dumps(cell, indent=4)))

    return notebook_new

def main():
    parser = argparse.ArgumentParser(description=textwrap.dedent("""
        Split up Jupyter Notebook to Sub-Notebooks by cell metadata.

        Specify tags to keep with `--keep`, specify tags to remove with `--remove`; multiple instances are ok. Special `--remove` tag: all (which removes all cells except those specified with `--keep`).
        All tags will be read from BASEKEY, which usually is `exercise`, if you do not specify it differently.
        """), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="Input file to parse (default: stdin)")
    parser.add_argument('--output', "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="Output file to parse to (default: stdout)")
    parser.add_argument('--keep',   "-k", action="append", help="Keep these tags (default: None)")
    parser.add_argument('--remove', "-r", action="append", help="Remove these tags. Special: all (remove all except for those of --keep). (default: None)")
    parser.add_argument('--basekey', type=str, help="Basekey to use for discriminating the tags (default: exercise)", default="exercise")
    parser.add_argument("-v", "--verbose", action='count', help="Verbose output; use multiple -v to increase verbosity; messages are printed to stderr (default: 0)", default=0)
    args = parser.parse_args()
    log_levels = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    log_level = log_levels[min(len(log_levels) - 1, args.verbose)]
    logger.setLevel(log_level)
    sh = logging.StreamHandler()
    sh.setLevel(log_level)
    sh.setFormatter(logging.Formatter('%(name)s::%(levelname)s::%(message)s'))
    logger.addHandler(sh)
    notebook = parse(inputfile=args.infile, keep=args.keep, remove=args.remove, basekey=args.basekey)

    json.dump(notebook, args.output, indent=1)

if __name__ == '__main__':
    main()
