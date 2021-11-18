from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import format_duration


def storage_information_view(request):
    non_closed_visits = []
    open_visits = Visit.objects.filter(leaved_at=None)
    for visit in open_visits:
        localtime_visit = localtime(visit.entered_at)
        non_closed_visits.append(dict(who_entered=visit.passcard.owner_name, entered_at=localtime_visit, duration=format_duration(visit.get_duration())))
    context = {
        'non_closed_visits': non_closed_visits,  # open visits (without leaved_at time)
    }
    return render(request, 'storage_information.html', context)
    