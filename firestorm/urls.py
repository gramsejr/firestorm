# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views_user import home, TopicCreate
from .views_kiosk import kiosk
from .views_user_profile import UserUpdate


urlpatterns = [
    # These are custom to the Firestorm project
    url(r'^$', home,
        name='home'),
    url(r'^kiosk/$', kiosk,
        name='kiosk'),
    url(r'^topic/create/$', TopicCreate.as_view(),
        name='topic_create'),
    url(r'^profile/edit/$', UserUpdate.as_view(),
        name='edit_profile', context={'subject_create_form':})
]
