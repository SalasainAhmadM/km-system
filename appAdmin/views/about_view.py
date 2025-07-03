from django.shortcuts import render, redirect
from django.urls import reverse
from appAdmin.models import About,AboutRationale, AboutObjective, AboutObjectiveDetail, AboutActivity, AboutTimeline, AboutTeamMember,AboutTeamSocial, AboutFooter, UploadVideo
from appAdmin.forms import AboutForm, AboutRationaleForm, AboutObjectiveForm, AboutObjectiveDetailForm, AboutActivityForm, AboutTimelineForm, AboutTeamMemberForm, AboutFooterForm, AboutTeamSocialForm, UploadForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from utils.user_control import user_access_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
# from appAdmin.forms import AboutForm

@user_access_required("admin")
def admin_main_about_page(request):
    videos = UploadVideo.objects.last()
    footer_content = AboutFooter.objects.all()
    context = {
            "footer_content": footer_content,
            "videos": videos,
        }

    return render(request, "pages/main-about.html")

@user_access_required("admin")
def admin_about_page(request):
    videos = UploadVideo.objects.last()
    about_content = About.objects.all().order_by('-date_created')
    footer_content = AboutFooter.objects.all()

    form = AboutForm()  # For the add modal
    # ✅ Build a dictionary of forms for each About item
    edit_forms = {item.about_id: AboutForm(instance=item) for item in about_content}

    context = {
        "about_content": about_content,
        "footer_content": footer_content,
        "videos": videos,
        "form": form,
        "edit_forms": edit_forms,  # ✅ Add to context
    }

    return render(request, "pages/about.html", context)

@user_access_required("admin")
def admin_about_add(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "About project added successfully!")
            return redirect("appAdmin:about-page")
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "pages/about.html", {
                "form": form,
                "about_content": About.objects.all().order_by('-date_created'),
                "footer_content": AboutFooter.objects.all(),
                "videos": UploadVideo.objects.last(),
                "show_add_modal": True
            })
    
    return redirect("appAdmin:about-page")

@user_access_required("admin")
def admin_about_edit(request, about_id):
    about_instance = get_object_or_404(About, about_id=about_id)
    
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "About project updated successfully!")
            return redirect("appAdmin:about-page")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AboutForm(instance=about_instance)
    
    context = {
        "form": form,
        "about_content": About.objects.all().order_by('-date_created'),
        "footer_content": AboutFooter.objects.all(),
        "videos": UploadVideo.objects.last(),
        "editing_item": about_instance,
        "show_edit_modal": True
    }
    
    return render(request, "pages/about.html", context)

@user_access_required("admin")
def admin_about_footer(request):
    footer_content = AboutFooter.objects.all()
    existing_instance = AboutFooter.objects.first()

    form = AboutFooterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print("FOOTER: ", form.cleaned_data)

        if existing_instance:
            return redirect("appAdmin:about-footer-edit")

        form.save()
        return redirect("appAdmin:about-page")

    if form.errors:
        print("FOOTER FORM ERRORS: ", form.errors)

    return render(
        request,
        "pages/about.html",
        {
            "form": form,
            "footer_content": footer_content,
            "form_action_footer": reverse(
                "appAdmin:about-footer-edit"
                if footer_content
                else "appAdmin:about-page"
            ),
        },
    )

@user_access_required("admin")
def admin_about_footer_edit(request):
    footer_instance = get_object_or_404(AboutFooter)
    form = AboutFooterForm(request.POST or None, instance=footer_instance)

    if request.method == "POST" and form.is_valid():
        print("EDIT FOOTER", form.cleaned_data)
        form.save()
        return redirect("appAdmin:about-page")

    if form.errors:
        print("FORM ERRORS:", form.errors)

    return render(request, "pages/about.html", {"form": form})

@user_access_required("admin")
def admin_upload_video(request):
    form = UploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Uploaded successfully!")
        return redirect("appAdmin:about-page")

    if form.errors:
        print("FORM ERRORS:", form.errors)

    return render(request, "pages/about.html", {"form": form})

# Edit About Project
@user_access_required("admin")
def admin_about_page_edit(request, about_id):
    about_instance = get_object_or_404(About, about_id=about_id)
    
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "About project updated successfully!")
            return redirect("appAdmin:about-page")
        else:
            messages.error(request, "Please correct the errors below.")

            # Repopulate necessary context for rendering about.html
            about_content = About.objects.all().order_by('-date_created')
            footer_content = AboutFooter.objects.all()
            videos = UploadVideo.objects.last()
            form = AboutForm(instance=about_instance)

            # ✅ Build edit_forms for all items
            edit_forms = {item.about_id: AboutForm(instance=item) for item in about_content}

            return render(request, "pages/about.html", {
                "form": AboutForm(),  # blank add form
                "about_content": about_content,
                "footer_content": footer_content,
                "videos": videos,
                "edit_forms": edit_forms,
                "show_edit_modal_id": about_id  # used to auto-open the modal
            })

    return redirect("appAdmin:about-page")

# Delete About Project
@user_access_required("admin")
@require_POST
def admin_about_delete(request, about_id):
    try:
        about_instance = get_object_or_404(About, about_id=about_id)
        project_name = about_instance.project_name
        about_instance.delete()
        messages.success(request, f"Project deleted successfully!")
    except Exception as e:
        messages.error(request, "Error deleting project. Please try again.")
    
    return redirect("appAdmin:about-page")

# Rationale View
@user_access_required("admin")
def about_rationale(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)
    rationale_items = AboutRationale.objects.filter(about_id=pk)

    form = AboutRationaleForm(initial={'about': about_instance})
    edit_forms = {item.rationale_id: AboutRationaleForm(instance=item) for item in rationale_items}

    context = {
        "about": about_instance,
        "rationale_items": rationale_items,
        "form": form,
        "edit_forms": edit_forms,
    }
    return render(request, "pages/about-rationale.html", context)


@user_access_required("admin")
def about_rationale_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutRationaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rationale added successfully!")
        else:
            messages.error(request, "Error adding rationale.")
    return redirect('appAdmin:about-rationale', pk=pk)


@user_access_required("admin")
def about_rationale_edit(request, rationale_id):
    rationale_item = get_object_or_404(AboutRationale, rationale_id=rationale_id)
    pk = rationale_item.about.about_id

    if request.method == "POST":
        form = AboutRationaleForm(request.POST, instance=rationale_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Rationale updated successfully!")
        else:
            messages.error(request, "Error updating rationale.")
    return redirect('appAdmin:about-rationale', pk=pk)


@user_access_required("admin")
@require_POST
def about_rationale_delete(request, rationale_id):
    rationale_item = get_object_or_404(AboutRationale, rationale_id=rationale_id)
    pk = rationale_item.about.about_id

    try:
        rationale_item.delete()
        messages.success(request, "Rationale deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting rationale.")
    
    return redirect('appAdmin:about-rationale', pk=pk)


# Objective View

@user_access_required("admin")
def about_objective(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    # Objective
    objective_items = AboutObjective.objects.filter(about_id=pk)
    objective_form = AboutObjectiveForm(initial={'about': about_instance})
    objective_edit_forms = {item.objective_id: AboutObjectiveForm(instance=item) for item in objective_items}

    # Objective Detail
    objectivedetail_items = AboutObjectiveDetail.objects.filter(about_id=pk)
    objectivedetail_form = AboutObjectiveDetailForm(initial={'about': about_instance})
    objectivedetail_edit_forms = {item.detail_id: AboutObjectiveDetailForm(instance=item) for item in objectivedetail_items}

    context = {
        "about": about_instance,
        "objective_items": objective_items,
        "objective_form": objective_form,
        "objective_edit_forms": objective_edit_forms,
        "objectivedetail_items": objectivedetail_items,
        "objectivedetail_form": objectivedetail_form,
        "objectivedetail_edit_forms": objectivedetail_edit_forms,
    }
    return render(request, "pages/about-objective.html", context)


# Objective CRUD

@user_access_required("admin")
def about_objective_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Objective added successfully!")
        else:
            messages.error(request, "Error adding objective.")
    return redirect('appAdmin:about-objective', pk=pk)


@user_access_required("admin")
def about_objective_edit(request, objective_id):
    objective_item = get_object_or_404(AboutObjective, objective_id=objective_id)
    pk = objective_item.about.about_id

    if request.method == "POST":
        form = AboutObjectiveForm(request.POST, instance=objective_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Objective updated successfully!")
        else:
            messages.error(request, "Error updating objective.")
    return redirect('appAdmin:about-objective', pk=pk)


@user_access_required("admin")
@require_POST
def about_objective_delete(request, objective_id):
    objective_item = get_object_or_404(AboutObjective, objective_id=objective_id)
    pk = objective_item.about.about_id

    try:
        objective_item.delete()
        messages.success(request, "Objective deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting objective.")
    
    return redirect('appAdmin:about-objective', pk=pk)


# Objective Detail CRUD

@user_access_required("admin")
def about_objectivedetail_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutObjectiveDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Objective detail added successfully!")
        else:
            messages.error(request, "Error adding objective detail.")
    return redirect('appAdmin:about-objective', pk=pk)


@user_access_required("admin")
def about_objectivedetail_edit(request, detail_id):
    objectivedetail_item = get_object_or_404(AboutObjectiveDetail, detail_id=detail_id)
    pk = objectivedetail_item.about.about_id

    if request.method == "POST":
        form = AboutObjectiveDetailForm(request.POST, instance=objectivedetail_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Objective detail updated successfully!")
        else:
            messages.error(request, "Error updating objective detail.")
    return redirect('appAdmin:about-objective', pk=pk)


@user_access_required("admin")
@require_POST
def about_objectivedetail_delete(request, detail_id):
    objectivedetail_item = get_object_or_404(AboutObjectiveDetail, detail_id=detail_id)
    pk = objectivedetail_item.about.about_id

    try:
        objectivedetail_item.delete()
        messages.success(request, "Objective detail deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting objective detail.")
    
    return redirect('appAdmin:about-objective', pk=pk)


# Activity View

@user_access_required("admin")
def about_activity(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)
    activity_items = AboutActivity.objects.filter(about_id=pk)

    form = AboutActivityForm(initial={'about': about_instance})
    edit_forms = {item.activity_id: AboutActivityForm(instance=item) for item in activity_items}

    context = {
        "about": about_instance,
        "activity_items": activity_items,
        "form": form,
        "edit_forms": edit_forms,
    }
    return render(request, "pages/about-activity.html", context)


@user_access_required("admin")
def about_activity_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutActivityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Activity added successfully!")
        else:
            messages.error(request, "Error adding activity.")
    return redirect('appAdmin:about-activity', pk=pk)


@user_access_required("admin")
def about_activity_edit(request, activity_id):
    activity_item = get_object_or_404(AboutActivity, activity_id=activity_id)
    pk = activity_item.about.about_id

    if request.method == "POST":
        form = AboutActivityForm(request.POST, instance=activity_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Activity updated successfully!")
        else:
            messages.error(request, "Error updating activity.")
    return redirect('appAdmin:about-activity', pk=pk)


@user_access_required("admin")
@require_POST
def about_activity_delete(request, activity_id):
    activity_item = get_object_or_404(AboutActivity, activity_id=activity_id)
    pk = activity_item.about.about_id

    try:
        activity_item.delete()
        messages.success(request, "Activity deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting activity.")
    
    return redirect('appAdmin:about-activity', pk=pk)

# Timeline View

@user_access_required("admin")
def about_timeline(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)
    timeline_items = AboutTimeline.objects.filter(about_id=pk)

    form = AboutTimelineForm(initial={'about': about_instance})
    edit_forms = {item.timeline_id: AboutTimelineForm(instance=item) for item in timeline_items}

    context = {
        "about": about_instance,
        "timeline_items": timeline_items,
        "form": form,
        "edit_forms": edit_forms,
    }
    return render(request, "pages/about-timeline.html", context)


@user_access_required("admin")
def about_timeline_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutTimelineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Timeline added successfully!")
        else:
            messages.error(request, "Error adding timeline.")
    return redirect('appAdmin:about-timeline', pk=pk)


@user_access_required("admin")
def about_timeline_edit(request, timeline_id):
    timeline_item = get_object_or_404(AboutTimeline, timeline_id=timeline_id)
    pk = timeline_item.about.about_id

    if request.method == "POST":
        form = AboutTimelineForm(request.POST, instance=timeline_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Timeline updated successfully!")
        else:
            messages.error(request, "Error updating timeline.")
    return redirect('appAdmin:about-timeline', pk=pk)


@user_access_required("admin")
@require_POST
def about_timeline_delete(request, timeline_id):
    timeline_item = get_object_or_404(AboutTimeline, timeline_id=timeline_id)
    pk = timeline_item.about.about_id

    try:
        timeline_item.delete()
        messages.success(request, "Timeline deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting timeline.")
    
    return redirect('appAdmin:about-timeline', pk=pk)

# Team View

# @user_access_required("admin")
# def about_team(request, pk):
#     about_instance = get_object_or_404(About, about_id=pk)
#     team_items = AboutTeamMember.objects.filter(about_id=pk)

#     context = {
#         "about": about_instance,
#         "team_items": team_items,
#     }
#     return render(request, "pages/about-team.html", context)

@user_access_required("admin")
def about_team(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)
    team_items = AboutTeamMember.objects.filter(about_id=pk)

    form = AboutTeamMemberForm(initial={'about': about_instance})
    edit_forms = {item.member_id: AboutTeamMemberForm(instance=item) for item in team_items}

    # Socials form per team member
    social_forms = {item.member_id: AboutTeamSocialForm() for item in team_items}

    context = {
        "about": about_instance,
        "team_items": team_items,
        "form": form,
        "edit_forms": edit_forms,
        "social_forms": social_forms,
    }
    return render(request, "pages/about-team.html", context)


@user_access_required("admin")
def about_team_add(request, pk):
    about_instance = get_object_or_404(About, about_id=pk)

    if request.method == "POST":
        form = AboutTeamMemberForm(request.POST, request.FILES)  
        if form.is_valid():
            team_member = form.save(commit=False)
            team_member.about = about_instance 
            team_member.save()
            messages.success(request, "Team added successfully!")
        else:
            messages.error(request, "Error adding team.")
    return redirect('appAdmin:about-team', pk=pk)


@user_access_required("admin")
def about_team_edit(request, member_id):
    team_item = get_object_or_404(AboutTeamMember, member_id=member_id)
    pk = team_item.about.about_id

    if request.method == "POST":
        form = AboutTeamMemberForm(request.POST, request.FILES, instance=team_item)  
        if form.is_valid():
            form.save()
            messages.success(request, "Team updated successfully!")
        else:
            messages.error(request, "Error updating team.")
    return redirect('appAdmin:about-team', pk=pk)


@user_access_required("admin")
@require_POST
def about_team_delete(request, member_id):
    team_item = get_object_or_404(AboutTeamMember, member_id=member_id)
    pk = team_item.about.about_id

    try:
        team_item.delete()
        messages.success(request, "Team deleted successfully!")
    except Exception:
        messages.error(request, "Error deleting team.")
    
    return redirect('appAdmin:about-team', pk=pk)

@user_access_required("admin")
@require_POST
def about_team_social_add(request, member_id):
    member = get_object_or_404(AboutTeamMember, member_id=member_id)
    pk = member.about.about_id

    form = AboutTeamSocialForm(request.POST)
    if form.is_valid():
        social = form.save(commit=False)
        social.member = member
        social.save()
        messages.success(request, "Social link added successfully!")
    else:
        messages.error(request, "Error adding social link.")
    return redirect('appAdmin:about-team', pk=pk)

@user_access_required("admin")
@require_POST
def about_team_social_delete(request, social_id):
    social = get_object_or_404(AboutTeamSocial, social_id=social_id)
    pk = social.member.about.about_id
    social.delete()
    messages.success(request, "Social link deleted successfully!")
    return redirect('appAdmin:about-team', pk=pk)

