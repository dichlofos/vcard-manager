#!/usr/bin/env python
# coding: utf-8

"""
    A wonderful piece of software to fix vCard files
"""

import vobject


def main():
    """
    Gravicappa
    """
    all_vcards = open('final-filtered.vcf').read()
    cards = vobject.readComponents(all_vcards)
    for card in cards:
        #print vobject.vcard.Name.toString(card.n.value)  ##. value.encode('utf-8')
        #print card.n.value.given  ##. value.encode('utf-8')
        #print card.n.value.prefix  ##. value.encode('utf-8')
        #print card.fn.value.encode('utf-8')
        #card.prettyPrint()
        #print card.serialize(lineLength=75)
        if getattr(card, "tel", None) is not None:
            for key in card.contents:
                if key not in ['version', 'n', 'fn', 'photo']:
                    # кошерно, содержит все повторения атрибута (списком)
                    values = card.contents[key]
                    for value in values:
                        print value
                    #print card.contents[key]
        #else:
        #    print card.tel


if __name__ == '__main__':
    main()

