from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from django.conf.urls.static import static
from django.conf import settings

"""List of urls that can be accessed from
http://http://127.0.0.1:8000/api/v1/.  Calls necessary
view functions for each URL.
"""

urlpatterns = [
	url(r"^users/$", CreateView.as_view(), name="create"),
	url(r"^users/(?P<pk>[0-9]+)/$", DetailsView.as_view(),
		name="details"),
	url(r"^rest-auth/", include("rest_auth.urls")),
	url(r"^rest-auth/registration/", include("rest_auth.registration.urls")),
	url(r"^user/", include("user_auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""Function enables a wider range of query strings
(e.g. http://127.0.0.1:8000/api/v1/users/1.json)
"""

urlpatterns = format_suffix_patterns(urlpatterns)