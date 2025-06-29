from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appCmi.views import home_view, get_input_from_search

app_name = "appCmi"

urlpatterns = (
    [
        path("home/", home_view.home, name="home"),
        path(
            "home/search",
            get_input_from_search,
            name="cmi-search",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
