#!/usr/bin/env bash
./filter.py > unix-filtered.vcf
cp unix-filtered.vcf final-filtered.vcf
