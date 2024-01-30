from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import Genre, Movie


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

#def movie_list(request):
 #   if request.method == 'POST':
 #       selected_genre_ids = request.POST.getlist('genres')
 #       selected_genres = Genre.objects.filter(id__in=selected_genre_ids)
 #       movies = Movie.objects.filter(genres__in=selected_genres).distinct()
 #       return render(request, 'movie_app/movie_list.html', {'movies': movies})
 #   else:
  #      genres = Genre.objects.all()
 #       return render(request, 'movie_app/select_genres.html', {'genres': genres})

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
            'genres': ['Action', 'Adventure'],
        },
        # Add more movie entries...
    ]

    return render(request, 'movie_app/movie_list.html', {'movies': movies})
