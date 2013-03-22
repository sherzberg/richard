#!/usr/bin/env python

import requests
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from richard.videos import models


BASE_URL = 'http://pyvideo.org'
CATEGORIES = BASE_URL + '/api/v1/category'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for tag_key in get_tags():
           tag, created = models.Tag.objects.get_or_create(tag=tag_key)
           print tag_key, 'created' if created else 'already had'


def get_categories():
    result = requests.get(CATEGORIES)
    result.raise_for_status()
    return result.json()['objects']


def get_videos(category):
    videos = []
    for video_key in category['videos']:
        video = requests.get(BASE_URL + video_key).json()
        videos.append(video)
    return videos


def get_tags():
    categories = get_categories()
    tags = []
    for category in categories:
        for video in get_videos(category):
            tags += video['tags']
    return set(tags)


if __name__ == '__main__':

    print(get_tags())
