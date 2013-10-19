from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
#from lighthouse.forms import *
#from lighthouse.models import *
from django.contrib.formtools.wizard.views import SessionWizardView
from django.forms.models import modelformset_factory, inlineformset_factory
from django.contrib import messages
#from django.contrib.messages.views import SuccessMessageMixin
from django.template.response import TemplateResponse, RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache

def start_page(request):
  # visitor main page
  return render(request, 'index.html', {})
