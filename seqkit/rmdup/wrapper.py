"""Snakemake wrapper for removing duplicated sequences by ID/name/sequence using seqkit"""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2023, Leighton Payne"
__email__ = "leighton@duck.com"
__license__ = "MIT"

from snakemake.shell import shell
import argparse

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
  "seqkit rmdup "
  "--threads {snakemake.threads} "
  "{extra} "
  "{snakemake.input} "
  "> {snakemake.output} "
  "{log}"
)
