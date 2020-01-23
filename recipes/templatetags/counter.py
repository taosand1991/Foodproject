from django import template
from recipes.models import Movie
register = template.Library()


@register.filter
def counter_movies(user):
    movie = Movie.objects.filter(profile=user).count()
    return movie

