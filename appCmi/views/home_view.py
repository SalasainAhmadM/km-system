from django.shortcuts import render
from appAdmin.models import About  # ✅ import the About model
from utils.get_models import get_active_models
from utils.user_control import user_access_required
from utils.search_function import find_similar_resources

@user_access_required(["admin", "cmi"], error_type=404)
def home(request):
    models = get_active_models()
    useful_links = models.get("useful_links", [])
    commodities = models.get("commodities", [])
    knowledge_resources = models.get("knowledge_resources", [])
    about_list = About.objects.all()  # ✅ include all About objects

    context = {
        "useful_links": useful_links,
        "commodities": commodities,
        "knowledge_resources": knowledge_resources,
        "about_list": about_list,  # ✅ pass it to the template
    }
    return render(request, "pages/home.html", context)


def get_input_from_search(request):
    query = request.GET.get("q", "").strip()

    if query:
        similar_resources = find_similar_resources(query)
    else:
        similar_resources = []

    context = {"query": query, "results": similar_resources}
    return render(request, "pages/cmi-search-result.html", context)
