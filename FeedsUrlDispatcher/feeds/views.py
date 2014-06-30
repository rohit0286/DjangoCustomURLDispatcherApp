

from dispatcher import BaseView
from dispatcher import dispatch
from django.core import serializers
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import Feed
import os


class HomeView(BaseView):

  @dispatch(request_type='GET', action='default')
  def getAllfeeds(self, request):
    template_file_path = 'templates/main.html'
    tmpl = os.path.join(os.path.dirname(__file__), template_file_path)
    return render_to_response(tmpl, {'feeds': Feed.objects.all()})

  @dispatch(request_type='POST', action='add')
  def addFeed(self, request):
    new_feed = Feed(title=request.POST.get('title'),
                    description=request.POST.get('description'))
    new_feed.save()
    return HttpResponse('Added Feed.')

  @dispatch(request_type='POST', action='delete')
  def deleteFeed(self, request):
    e_feed = Feed.objects.filter(title=request.POST.get('title'))
    e_feed.delete()
    return HttpResponse('Deleted Feed.')
