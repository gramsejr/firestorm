# -*- coding: utf-8 -*-
"""views_user.py represents the user-interface Pythonic logic.

This is the views_user.py which represents the Python logic for views
that refer specifically to a user's interaction with the application.
Kiosk views are held in another file and do not belong in here.
"""
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .forms import ProfileForm
from .models import User
from .mixins import AjaxableResponseMixin


class UserUpdate(UpdateView):
    model = User
    fields = ['password', 'email', 'first_name', 'last_name']
    template_name = 'profile/edit.html'


@login_required
def profile(request):
    """profile is the place you go to change your info
    
    Uses django user
    """
    user_data = UpdateView(request.user)
    context = {'subject_create_form': ProfileForm(),
               'user_data': user_data}
    return render(request, 'user/index.html', context)
