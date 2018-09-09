from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r"^auth/", include("rest_framework.urls",
		namespace="rest_framework")),
	url(r"^users/$", CreateView.as_view(), name="create"),
	url(r"^users/(?P<pk>[0-9]+)/$", DetailsView.as_view(),
		name="details"),
	url(r"^user/$", UserView.as_view(), name="user"),
	url(r"^user/(?P<pk>[0-9]+)/$", UserDetailsView.as_view(),
		name="user_details"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)