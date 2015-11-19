from django import shortcuts
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from bots.abridged_bot import DIR_PATH as BOT_PATH
import random, os, re
from settings.common import PROJECT_PATH, SECRETS_DICT, ADMIN_EMAILS, getTrueSpeakBucket, getOrCreateS3Key
from common import send_mailgun_message
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from boto.s3.connection import S3Connection, Key
import stripe, json, mailchimp


# abridged space #######################################################################################################
@ensure_csrf_cookie
def abridged_space(request, coordinates=None):
    return render(request, 'abridged_space.html', {'coordinates': coordinates})

def abridged_space2(request, coordinates=None):
    return render(request, 'abridged_space2.html', {'coordinates': coordinates})

@csrf_exempt
def abridged_space_take_me_anywhere(request):
    cities_file_path = os.path.join(BOT_PATH, 'world_cities.csv')
    with open(cities_file_path, 'r') as cities_file:
        cities = []
        for line in cities_file:
            cities.append(line)

    # randomly choose
    which_city = random.choice(cities)
    which_city = which_city.replace('"', '')
    num, country, city, lat, lon, _ = which_city.split(';')
    if request.method == 'POST':
        place_str = city + ', ' + country
        return HttpResponse(json.dumps({
            'lat': lat,
            'lon': lon,
            'place_str': place_str
        }))
    else:
        return shortcuts.redirect('/gmaps/{},{},{}/'.format(str(lat), str(lon), '15'))


def redirect(request, page='/home'):
    return shortcuts.redirect(page)