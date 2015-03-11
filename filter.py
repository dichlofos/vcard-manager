#!/usr/bin/env python
# coding: utf-8

"""
    A wonderful piece of software to fix vCard files
"""


def main():
    """
    Gravicappa
    """
    unk_index = 0

    with open('unix.vcf') as vcf_file:
        for line in vcf_file:
            line = line.rstrip()

            # fix some Android export bugs
            if line == 'ORG:':
                # skip it; delete; delete!
                continue
            if line == 'N:':
                line = 'N:Unknown_' + str(unk_index) + ';;;;'
                unk_index = unk_index + 1
            if line == 'FN:':
                line = 'FN:Unknown_' + str(unk_index) + ';;;;'
                unk_index = unk_index + 1
            print line


if __name__ == '__main__':
    main()
