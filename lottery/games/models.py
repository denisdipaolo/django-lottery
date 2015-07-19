from random import randint

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.aggregates import Count

from . import helpers

# Create your models here.
class GameManager(models.Manager):
    use_for_related_fields = True


    def available_games(self, user, **kwargs):
        return self.exclude(winner__isnull=False).exclude(partecipants=user).filter(date__gt=timezone.now())

    def games_to_draw(self, **kwargs):
        return self.filter(winner__isnull=True).filter(date__lt=timezone.now())

class Game(models.Model):
    name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    partecipants = models.ManyToManyField(User, through='partecipation.Partecipation', related_name='game_partecipant')
    date = models.DateTimeField(default=helpers.default_date())

    objects = GameManager()


    def clean(self):
        if timezone.now() > self.date:
            raise ValidationError('Game date cannot be in the past.')

    def draw_winners(self):
        for past_game in Game.objects.games_to_draw():
            count = past_game.partecipants.aggregate(count=Count('id'))['count']
            if count:
                random_index = randint(0, count - 1)
                winner = Winner(game=past_game, user=past_game.partecipants.all()[random_index])
                winner.save()

    def __unicode__(self):
        return self.name

class Winner(models.Model):
    game = models.OneToOneField(Game)
    user = models.ForeignKey(User)