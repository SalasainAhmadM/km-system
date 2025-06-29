from django.shortcuts import render, get_object_or_404
from appAdmin.models import About, UploadVideo, CMI, AboutRationale, AboutObjective, AboutObjectiveDetail, AboutActivity , AboutTimeline, AboutTeamMember, AboutTeamSocial
from utils.get_models import get_active_models
from utils.user_control import user_access_required


@user_access_required(["admin", "cmi"], error_type=404)
def cmi_about(request, about_id):
    about = get_object_or_404(About, pk=about_id)
    videos = UploadVideo.objects.last()
    cmis = CMI.objects.filter(status="active")
    models = get_active_models()

    # 🔥 Fetch all rationale matching this about_id
    rationales = AboutRationale.objects.filter(about_id=about_id)
    objectives = AboutObjective.objects.filter(about_id=about_id)
    objectivesdetail = AboutObjectiveDetail.objects.filter(about_id=about_id)
    activities = AboutActivity.objects.filter(about_id=about_id)
    timelines = AboutTimeline.objects.filter(about_id=about_id)
    team_members = AboutTeamMember.objects.filter(about_id=about_id).prefetch_related('socials')

    context = {
        "about": about,
        "videos": videos,
        "cmis": cmis,
        "useful_links": models.get("useful_links", []),
        "commodities": models.get("commodities", []),
        "knowledge_resources": models.get("knowledge_resources", []),
        "about_list": About.objects.all(),
        "rationales": rationales,
        "objectives": objectives, 
        "objectivesdetail": objectivesdetail, 
        "activities": activities, 
        "timelines": timelines,
        "team_members": team_members, 
    }
    return render(request, "pages/cmi-about.html", context)
