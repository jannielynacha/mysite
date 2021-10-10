from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Review, Critic, Link, Multimedia

# Create your views here.
def index(request):
	current_user = request.user
	review_list = Review.objects.order_by('-publication_date')[:5]
	template = loader.get_template('reviews/index.html')
	context = {
		'review_list': review_list,
		'user': current_user
	}
	return HttpResponse(template.render(context, request))