# coding: utf-8
"""
VCM Views
"""

#from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from vcm.models import Card

import vobject


def index(request):

    return HttpResponse("QQQ")


def cards(request):
    """Show all vCards"""

    cards = Card.objects.all()

    return render(request, 'vcm/cards.html', {
        'cards': cards,
    })


def load(request):
    """Load vCards from submitted file"""

    # load
    all_vcards = open('../final-filtered.vcf').read()
    cards = vobject.readComponents(all_vcards)
    for card in cards:
        card_db = Card()
        #print vobject.vcard.Name.toString(card.n.value)  ##. value.encode('utf-8')
        #print card.n.value.given  ##. value.encode('utf-8')
        #print card.n.value.prefix  ##. value.encode('utf-8')
        #print card.fn.value.encode('utf-8')
        #card.prettyPrint()
        #print card.serialize(lineLength=75)
        if getattr(card, "tel", None) is not None:
            card_db.family_name = card.fn
            for key in card.contents:
                if key not in ['version', 'n', 'fn', 'photo']:
                    # кошерно, содержит все повторения атрибута (списком)
                    values = card.contents[key]
                    for value in values:
                        print value
                    #print card.contents[key]
            card_db.save()
        #else:
        #    print card.tel

    # on successful load
    return HttpResponseRedirect('/vcm/cards/')
