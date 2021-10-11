from django .urls import path

from reviews.api.views import api_detail_review_view, api_detail_critic_view

app_name = 'reviews'

urlpatterns = [
	path('<int:id>/', api_detail_review_view, name='detail'),
	path('<int:id>/critic/', api_detail_critic_view, name='critic_detail')
]
