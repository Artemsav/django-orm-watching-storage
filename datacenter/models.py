from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        entered_at = self.entered_at
        leaved_at = self.leaved_at
        localtime_entered_at = localtime(entered_at)
        if leaved_at:
            localtime_leave_at = localtime(leaved_at)
            delta = localtime_leave_at - localtime_entered_at
        else:
            delta = localtime() - localtime_entered_at
        return delta.total_seconds()

    def is_visit_long(self, minutes=60):
        return (self.get_duration() // 60) > minutes       

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )


def format_duration(duration):
        # format duration in seconds in the following format 8ч 25м
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        return '{hours}ч {minutes}м'.format(hours=int(hours), minutes=int(minutes))
