from django import forms
from django.db import models
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm
from django.urls import reverse
from basicApp.models import Donate


class DonateBook(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['Branch','Year','Subject','Publication','Author','Subject_code','Image']
