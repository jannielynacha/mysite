from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reviews.models import Review, Critic, Link, Multimedia
from reviews.serializers import ReviewSerializer

@api_view(['GET', ])
def api_detail_review_view(request, id):

	try:
		review = Review.objects.get(id=id)
	except Review.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = ReviewSerializer(review)
		return Response(serializer.data)

@api_view(['GET', ])
def api_detail_critic_view(request, id):

	try:
		critic = Critic.objects.get(id=id)
	except Critic.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = CriticSerializer(critic)
		return Response(serializer.data)