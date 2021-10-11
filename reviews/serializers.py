from django.contrib.auth.models import User
from reviews.models import Review, Critic
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

class CriticSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Critic
		fields = '__all__'