from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Critic(models.Model):
	display_name = models.CharField(max_length=100)
	sort_name = models.CharField(max_length=100)
	status = models.CharField(max_length=10)
	bio = models.CharField(max_length=300)
	seo_name = models.CharField(max_length=200)


class Review(models.Model):
	display_title = models.CharField(max_length=5000)
	mpaa_rating = models.CharField(max_length=100)
	critics_pick = models.IntegerField()
	byline = models.ForeignKey(Critic, on_delete=models.CASCADE)
	headline = models.CharField(max_length=400)
	summary_short = models.CharField(max_length=500)
	publication_date = models.CharField(max_length=100)
	opening_date = models.CharField(max_length=100)
	date_updated = models.CharField(max_length=100)
	review_text = models.CharField(max_length=200)
	bookmark = models.ManyToManyField(User, related_name='bookmark', blank=True)

class Link(models.Model):
	review = models.OneToOneField(Review, on_delete=models.CASCADE, primary_key=True)
	type = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	suggested_link_text = models.CharField(max_length=500)


class Multimedia(models.Model):
	review = models.OneToOneField(Review, on_delete=models.CASCADE, primary_key=True)
	type = models.CharField(max_length=100)
	src = models.CharField(max_length=500)
	height = models.IntegerField()
	width = models.IntegerField()