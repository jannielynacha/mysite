from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    display_title = serializers.CharField(max_length=5000)
	mpaa_rating = serializers.CharField(max_length=100)
	critics_pick = serializers.IntegerField()
	byline = serializers.ForeignKey(Critic, on_delete=serializers.CASCADE)
	headline = serializers.CharField(max_length=400)
	summary_short = serializers.CharField(max_length=500)
	publication_date = serializers.CharField(max_length=100)
	opening_date = serializers.CharField(max_length=100)
	date_updated = serializers.CharField(max_length=100)
	review_text = serializers.CharField(max_length=200)
	bookmark = serializers.ManyToManyField(User, related_name='bookmark', blank=True)

def create(self, validated_data):
	"""
	Create and return a new `Review` instance, given the validated data.
	"""
	return Review.objects.create(**validated_data)

def update(self, instance, validated_data):
"""
	Update and return an existing `Review` instance, given the validated data.
	"""
	instance.display_title = validated_data.get('display_title', instance.display_title)
	instance.mpaa_rating = validated_data.get('mpaa_rating', instance.mpaa_rating)
	instance.critics_pick = validated_data.get('critics_pick', instance.critics_pick)
	instance.byline = validated_data.get('byline', instance.byline)
	instance.headline = validated_data.get('headline', instance.headline)
	instance.summary_short = validated_data.get('summary_short', instance.summary_short)
	instance.publication_date = validated_data.get('publication_date', instance.publication_date)
	instance.opening_date = validated_data.get('opening_date', instance.opening_date)
	instance.date_updated = validated_data.get('date_updated', instance.date_updated)
	instance.review_text = validated_data.get('review_text', instance.review_text)
	instance.bookmark = validated_data.get('bookmark', instance.bookmark)

	instance.save()
	return instance