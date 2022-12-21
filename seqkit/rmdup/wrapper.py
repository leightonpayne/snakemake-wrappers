"""Snakemake wrapper for removing duplicated sequences by ID/name/sequence using seqkit"""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2022, Leighton Payne"
__email__ = "leightonpayne98@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import argparse

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Parse command line arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-n", "--by-name", action="store_true", help="enable flag --by-name")
group.add_argument("-s", "--by-seq", action="store_true", help="enable flag --by-seq")
args = parser.parse_args()

# Determine which flag was called
if args.by_name:
    flag = "--by-name"
elif args.by_seq:
    flag = "--by-seq"

shell("f(seqkit rmdup {flag} {extra} ) {log}")
