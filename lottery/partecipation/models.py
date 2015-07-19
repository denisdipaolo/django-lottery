from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from games.models import Game

# Create your models here.
class Partecipation(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    def __unicode__(self):
        return '{} partecipating {}'.format(self.user.username, self.game.name)

    class Meta:
        unique_together = ('user', 'game')