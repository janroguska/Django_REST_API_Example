from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r"^users/$", CreateView.as_view(), name="create"),
	url(r"^users/(?P<pk>[0-9]+)/$", DetailsView.as_view(),
		name="details"),
	url(r"^rest-auth/", include("rest_auth.urls")),
	url(r"^rest-auth/registration/", include("rest_auth.registration.urls")),
	url(r"^user/", include("user_auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)