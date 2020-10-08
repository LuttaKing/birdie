from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import LastTweetID
from django.utils import timezone


@csrf_exempt
def update_last_id(request):
    if request.method == 'POST':
        
        new_tweetID=request.POST.get('new_tweetID')
        old_tweetID=request.POST.get('old_tweetID')
        try:
                    tweetModel=LastTweetID.objects.get(tweetId=old_tweetID)
                    tweetModel.tweetId=new_tweetID
                 #   tweetModel.time=timezone.now
                    tweetModel.save()
        
        except LastTweetID.DoesNotExist:
                    print('That tweet ID does not exist')
        return HttpResponse('Posted')
    else:
        last_tweetModel=LastTweetID.objects.all().last()
        print(last_tweetModel)
        Id=last_tweetModel.tweetId

        return HttpResponse(Id)
        

