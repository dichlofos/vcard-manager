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
            if not line:
                continue
            elif line.startswith('END:VCARD'):
                print line
                # skip one empty line between cards, by RFC
                print
                continue
            elif line.startswith('PHOTO;'):
                line = line.replace('ENCODING=B', 'ENCODING=b')
            elif line == 'N:':
                line = 'N:Unknown_' + str(unk_index) + ';;;;'
                unk_index = unk_index + 1
            elif line == 'FN:':
                line = 'FN:Unknown_' + str(unk_index) + ';;;;'
                unk_index = unk_index + 1
            print line


if __name__ == '__main__':
    main()
