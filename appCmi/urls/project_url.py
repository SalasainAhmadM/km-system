# appCmi/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appCmi.views import project_sub_view, home_view,project_view

app_name = "appCmi"

urlpatterns = [
    # Main project detail page
    path("project/<int:about_id>/", project_view.project_detail, name="project"),
    
    # Subproject detail page
    path('project-sub/<int:sub_id>/', project_view.project_sub_view, name='project-sub'),
    
    # Home page
    path("home/", home_view.home, name="home"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)