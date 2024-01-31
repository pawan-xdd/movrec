from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import Genre, Movie
import pandas as pd


def homepage(request):
    return render(request, 'movie_app/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    context = {'registerForm': form}

    return render(request, 'movie_app/register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform': form}

    return render(request, 'movie_app/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("")


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'movie_app/dashboard.html')


movie_csv = pd.read_csv('movie_app/movies.csv')


def movie_list(request):
    movies = [
        {
            'title': 'Inception',
            'poster_url': 'https://m.media-amazon.com/images/I/51j6r6qLH0S._SX300_SY300_QL70_FMwebp_.jpg',
            'synopsis': """
            "Inception," directed by Christopher Nolan, is a captivating science fiction thriller that revolves around Dom Cobb, 
            a skilled extractor played by Leonardo DiCaprio. Cobb leads a team of specialists into the uncharted territory of dreams to 
            perform 'inception' – the planting of an idea into someone's mind. As they navigate through layers of subconscious realities, 
            the film blurs the lines between dreams and reality, delivering a visually stunning and intellectually engaging experience. 
            Cobb's personal struggles, particularly with the specter of his deceased wife, add emotional depth to the intricate plot, 
            making "Inception" a cinematic masterpiece known for its mind-bending narrative and innovative storytelling.
            """,
            'rating': '8.5',
            #'genres': ['Action', 'Adventure'],
        },

        # Add more movie entries...
    ]
    # suggestion = random.choice(movies)
    return render(request, 'movie_app/movie_list.html', {'movies': movies})


def movie_list2(request):
    movies = [
        {
            'title': 'The Shawshank Redemption',
            'poster_url': 'https://i.pinimg.com/474x/57/62/e7/5762e78c67816b179da5f43fc566ae95.jpg',
            'synopsis': """
            "The Shawshank Redemption," directed by Frank Darabont, is a poignant tale of resilience and friendship set 
            within the confines of Shawshank State Penitentiary. The film follows Andy Dufresne, played by Tim Robbins, 
            a banker convicted of a crime he didn't commit. As Andy adapts to the harsh realities of prison life, he 
            befriends fellow inmate Ellis "Red" Redding, portrayed by Morgan Freeman. Andy's intelligence and 
            determination lead him to carve out a unique place for https://imgur.com/a/VBxmhEphimself within the prison community, offering hope 
            and a sense of purpose to his fellow inmates. The story unfolds as Andy meticulously plans his escape, 
            revealing the transformative power of hope and the enduring spirit of the human soul. 
            "The Shawshank Redemption" is celebrated for its powerful performances, compelling characters, and a 
            narrative that explores the indomitable nature of the human spirit against all odds.
            """,
            'rating': '9.3',
            #'genres': ['Thriller', 'Drama'],
        },

        # Add more movie entries...
    ]
    # suggestion = random.choice(movies)
    return render(request, 'movie_app/movie_list2.html', {'movies': movies})


def movie_list3(request):
    movies = [
        {
            'title': 'Pulp Fiction',
            'poster_url': "https://i.pinimg.com/474x/82/48/dd/8248ddf19710eae0c772482cee9c1419.jpg",
            'synopsis': """The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits 
                        intertwine in four tales of violence and redemption.""",
            'rating': '8.9',
            #'genres': ['Action', 'Crime'],
        },

        # Add more movie entries...
    ]
    # suggestion = random.choice(movies)
    return render(request, 'movie_app/movie_list3.html', {'movies': movies})


def movie_list4(request):
    movies = [
        {
            'title': 'The Dark Knight',
            'poster_url': 'https://i.pinimg.com/474x/d6/15/94/d61594e30a71157c07a762b471824bd7.jpg',
            'synopsis': """
            When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one 
            of the greatest psychological and physical tests of his ability to fight injustice.""",
            'rating': '8.9',
            #'genres': ['Action', ],
        },

        # Add more movie entries...
    ]
    # suggestion = random.choice(movies)
    return render(request, 'movie_app/movie_list4.html', {'movies': movies})


def movie_list5(request):
    movies = [
        {
            'title': 'Forrest Gump',
            'poster_url': 'https://i.pinimg.com/474x/77/e7/36/77e736cb6aaf98b6b43637f088005c5e.jpg',
            'synopsis': """
            The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man 
            with an IQ of 75, who yearns to be reunited with his childhood sweetheart.""",
            'rating': '8.5',
            #'genres': ['Drama', ],
        },

        # Add more movie entries...
    ]
    # suggestion = random.choice(movies)
    return render(request, 'movie_app/movie_list5.html', {'movies': movies})


def about(request):
    return render(request, 'movie_app/about.html')