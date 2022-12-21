"""Snakemake wrapper for removing duplicated sequences by ID/name/sequence using seqkit"""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2022, Leighton Payne"
__email__ = "leightonpayne98@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import argparse

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

by = snakemake.params.get("by", "")
if by == "sequence":
    flag = "--by-seq"
elif by == "name":
    flag = "--by-name"

shell("(seqkit rmdup {flag} {extra} {snakemake.input} > {snakemake.output}) {log}")
