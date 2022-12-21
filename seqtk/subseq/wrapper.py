"""Snakemake wrapper for extracting subsequences from FASTA/Q using seqtk"""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2022, Leighton Payne"
__email__ = "leightonpayne98@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("(seqtk subseq {extra} {snakemake.input.faa} {snakemake.input.list} > {snakemake.output}) {log})"
