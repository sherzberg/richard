from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from richard.videos import sampledata


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        sampledata.generate_sampledata({})
