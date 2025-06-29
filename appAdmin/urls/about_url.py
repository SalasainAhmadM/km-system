from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appAdmin.views import about_view
app_name = "appAdmin"

urlpatterns = (
    [
        # Rationale URLs
        path('about-rationale/<int:pk>/', about_view.about_rationale, name='about-rationale'),
        path('about-rationale/<int:pk>/add/', about_view.about_rationale_add, name='about-rationale-add'),
        path('about-rationale/edit/<int:rationale_id>/', about_view.about_rationale_edit, name='about-rationale-edit'),
        path('about-rationale/delete/<int:rationale_id>/', about_view.about_rationale_delete, name='about-rationale-delete'),

        # Objective
        path('about-objective/<int:pk>/', about_view.about_objective, name='about-objective'),
        path('about-objective/<int:pk>/add/', about_view.about_objective_add, name='about-objective-add'),
        path('about-objective/edit/<int:objective_id>/', about_view.about_objective_edit, name='about-objective-edit'),
        path('about-objective/delete/<int:objective_id>/', about_view.about_objective_delete, name='about-objective-delete'),

        # Objective Detail (No separate page needed)
        path('about-objective/<int:pk>/detail/add/', about_view.about_objectivedetail_add, name='about-objectivedetail-add'),
        path('about-objective/detail/edit/<int:detail_id>/', about_view.about_objectivedetail_edit, name='about-objectivedetail-edit'),
        path('about-objective/detail/delete/<int:detail_id>/', about_view.about_objectivedetail_delete, name='about-objectivedetail-delete'),

        # Activity URLs
        path('about-activity/<int:pk>/', about_view.about_activity, name='about-activity'),
        path('about-activity/<int:pk>/add/', about_view.about_activity_add, name='about-activity-add'),
        path('about-activity/edit/<int:activity_id>/', about_view.about_activity_edit, name='about-activity-edit'),
        path('about-activity/delete/<int:activity_id>/', about_view.about_activity_delete, name='about-activity-delete'),

        # Timeline URLs
        path('about-timeline/<int:pk>/', about_view.about_timeline, name='about-timeline'),
        path('about-timeline/<int:pk>/add/', about_view.about_timeline_add, name='about-timeline-add'),
        path('about-timeline/edit/<int:timeline_id>/', about_view.about_timeline_edit, name='about-timeline-edit'),
        path('about-timeline/delete/<int:timeline_id>/', about_view.about_timeline_delete, name='about-timeline-delete'),

        # Team URLs
        path('about-team/<int:pk>/', about_view.about_team, name='about-team'),
        path('about-team/<int:pk>/add/', about_view.about_team_add, name='about-team-add'),
        path('about-team/edit/<int:member_id>/', about_view.about_team_edit, name='about-team-edit'),
        path('about-team/delete/<int:member_id>/', about_view.about_team_delete, name='about-team-delete'),

        # Team Social URLs
        path('about-team/social/add/<int:member_id>/', about_view.about_team_social_add, name='about-team-social-add'),
        path('about-team/social/delete/<int:social_id>/', about_view.about_team_social_delete, name='about-team-social-delete'),


        path("about/page/edit/<int:about_id>/", about_view.admin_about_page_edit, name="about-page-edit"),

        path("about/", about_view.admin_about_page, name="about-page"),
        path("about/add/", about_view.admin_about_add, name="about-add"),
        path("about/edit/<int:about_id>/", about_view.admin_about_edit, name="about-edit"),
        path("about/delete/<int:about_id>/", about_view.admin_about_delete, name="about-delete"),
        path("footer/", about_view.admin_about_footer, name="about-footer"),
        path(
            "footer/edit/", about_view.admin_about_footer_edit, name="about-footer-edit"
        ),
        path("upload-video/", about_view.admin_upload_video, name="admin-video-upload"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)