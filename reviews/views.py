from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from reviews.serializers import UserSerializer
from .models import Review, Critic, Link, Multimedia
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	current_user = request.user
	template = loader.get_template('reviews/index.html')
	review_list = Review.objects.order_by('-publication_date')
	review_list_bookmarked = current_user.bookmark.all()
	p = Paginator(review_list, 10)
	# page_number = request.GET.get('page')
	# page_obj = paginator.get_page(page_number)

	page = p.page(2)

	context = {
		'review_list': review_list,
		'user': current_user,
		'review_list_bookmarked': review_list_bookmarked
	}
	return HttpResponse(template.render(context, request))

def bookmarksview(request):
	current_user = request.user
	template = loader.get_template('reviews/bookmarks.html')
	review_list = current_user.bookmark.all()

	context = {
		'bookmarked_review': review_list,
		'user': current_user
	}
	
	return HttpResponse(template.render(context, request))

def addbookmark(request):
	review_id = request.GET.get('id')
	review = get_object_or_404(Review, id=review_id)
	if review.bookmark.filter(id=review_id).exists():
		review.bookmark.remove(request.user)
	else:
		review.bookmark.add(request.user)

	return HttpResponseRedirect(reverse(index))


class ReviewSearchView(ListView):
	model =  Review
	template = 'index.html'

	def get_queryset(self):
		query = self.request.GET.get('search_term')
		return Review.objects.filter(display_title__icontains=query)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]