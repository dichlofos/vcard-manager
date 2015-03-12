#!/usr/bin/env bash
cp 00001.vcf unix.vcf
dos2unix unix.vcf
./filter.py > unix-filtered.vcf
cp unix-filtered.vcf final-filtered.vcf
