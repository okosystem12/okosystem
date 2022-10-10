from django.contrib import auth
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def auth_logout(request):
    auth.logout(request)
    return redirect('/')
