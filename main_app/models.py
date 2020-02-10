from django.db import models
from django.urls import reverse
from datetime import date, datetime
# Create your models here.

PRACTICES = (
    ('T', 'Toy Problem'),
    ('P', 'Project'),
    ('A', 'Application')
)

class Language(models.Model):
    name = models.CharField(max_length = 100)
    years_experience = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'language_id': self.id})
    def skilled_enough(self):
        return self.upskill_set.filter(date=date.today()).count() >= len(PRACTICES)

class Upskill(models.Model):
  date = models.DateField()
  practice = models.CharField(max_length=1, choices=PRACTICES, default = PRACTICES[0][0])
  language = models.ForeignKey(Language, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_practice_display()} on {self.date}"
  #change the default sort
  class Meta:
    ordering = ['-date']