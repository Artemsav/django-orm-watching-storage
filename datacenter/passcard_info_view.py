from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    this_passcard_visits = []
    visiter_card = dict(passcard=passcard[0])
    for visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits.append(dict(entered_at=visit.entered_at, duration=format_duration(visit.get_duration()), is_strange=visit.is_visit_long()))
    context = {
        'passcard': visiter_card,  # Visiter's passcard
        'this_passcard_visits': this_passcard_visits  # List of visits for this passcard
    }
    return render(request, 'passcard_info.html', context)
