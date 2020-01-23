from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
import json
import requests
from recipes.form import MovieForm
from .models import Movie
from django.contrib import messages
from .form import LoginForm
from django.forms.models import model_to_dict
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(request):
    url = 'http://www.omdbapi.com/?apikey=da403238&t={}'
    if request.method == 'GET':
        t = request.GET.get('query')
    else:
        t = request.GET.get('query')
    response = requests.get(url.format(t)).json()
    movies_data = []
    try:
        movies = {
            'title': response['Title'],
            'year': response['Year'],
            'rated': response['Rated'],
            'runtime': response['Runtime'],
            'genre': response['Genre'],
            'director': response['Director'],
            'writer': response['Writer'],
            'actors': response['Actors'],
            'language': response['Language'],
            'country': response['Country'],
            'awards': response['Awards'],
            'poster': response['Poster'],
            'ratings': response['Ratings'][0],
        }
    except:
        movies = 'not found'
    movies_data.append(movies)
    context = {'movies_data': movies_data}
    template = 'recipes/home.html'
    return render(request, template, context)


def search_result(request):
    url = 'http://www.omdbapi.com/?apikey=da403238&t={}'
    if request.method == "GET" and request.is_ajax():
        t = request.GET.get('query')
    else:
        t = request.GET.get('query')
    template = 'recipes/search.html'
    movies_data = []
    try:
        response = requests.get(url.format(t)).json()
        movies = {
            'title': response['Title'],
            'year': response['Year'],
            'rated': response['Rated'],
            'runtime': response['Runtime'],
            'genre': response['Genre'],
            'director': response['Director'],
            'writer': response['Writer'],
            'actors': response['Actors'],
            'language': response['Language'],
            'country': response['Country'],
            'awards': response['Awards'],
            'poster': response['Poster'],
            'ratings': response['Ratings'][0]['Source'],
            'ratings_2': response['Ratings'][0]['Value'],
        }
    except:
        return HttpResponse('<center>The movie cannot be found on this server</center>')
    movies_data.append(movies)
    context = {'movies_data': movies_data}
    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def add_movie(request):
    movies = Movie.objects.filter(profile=request.user)

    url = 'http://www.omdbapi.com/?apikey=da403238&t={}'

    form = MovieForm(data=request.POST or None)
    if form.is_valid():
        new_movie = form.cleaned_data.get('movie')
        response = requests.get(url.format(new_movie)).json()
        if response['Response'] == 'False':
            messages.error(request, 'The movie is not found')
        elif Movie.objects.filter(profile=request.user, movie=new_movie).exists():
            messages.error(request, 'You have this movie in your account already')
        else:
            use = form.save(commit=False)
            use.profile = request.user
            use.save()
            messages.success(request, 'your movie has been added')
    form = MovieForm()
    movies_data = []
    for movie in movies:
        response = requests.get(url.format(movie)).json()
        movies = {
            'title': movie,
            'year': response['Year'],
            'rated': response['Rated'],
            'runtime': response['Runtime'],
            'genre': response['Genre'],
            'director': response['Director'],
            'writer': response['Writer'],
            'actors': response['Actors'],
            'language': response['Language'],
            'country': response['Country'],
            'awards': response['Awards'],
            'poster': response['Poster'],
            'ratings': response['Ratings'][0]['Source'],
            'ratings_2': response['Ratings'][0]['Value'],
        }
        movies_data.append(movies)
    data = {'movies_data': movies_data, 'form': form
               }
    return render(request, 'recipes/add_movie.html', data)


def delete_movie(request, movie_name):
    Movie.objects.get(profile=request.user, movie=movie_name).delete()
    messages.error(request, 'Your movie has been deleted')
    return redirect('add')



# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             messages.success(request, 'Your login was successful')
#             return redirect('home')
#     form = LoginForm()
#     return render(request, 'recipes/login.html', {'form': form})

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    redirect_authenticated_user = settings.LOGIN_REDIRECT_URL


# def logout_user(request):
#     logout(request)
#     return redirect('home')