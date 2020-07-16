import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers import UserSerializer
from main import authenticators
from main.forms import SignupForm

logging.basicConfig(filename="test.log", level=logging.DEBUG)


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def index(request):
    return HttpResponse("")


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def profile(request):
    return HttpResponse("{page: profile}")


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def create_account_category(request):
    current_user = request.user
    return HttpResponse(current_user.id)


@login_required(login_url='/api-auth/')
@api_view(['GET'])
@ensure_csrf_cookie
def get_account(request):
    current_user = request.user
    return Response(UserSerializer(current_user).data)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class AuthView(APIView):
    authentication_classes = (authenticators.QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            user_data = json.loads(request.body)
            user = authenticate(username=user_data['username'], password=user_data['password'])
            request.user = user
            login(request, request.user)
            return Response(UserSerializer(request.user).data)
        except:
            return HttpResponseBadRequest(json.dumps({'error': 'bad request'}), content_type="application/json")


def delete(self, request, *args, **kwargs):
    logout(request)
    return Response()
