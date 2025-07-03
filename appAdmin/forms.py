from .models import (
    Commodity,
    KnowledgeResources,
    About,
    AboutFooter,
    CMI,
    UploadVideo,
    UsefulLinks,
    ResourceMetadata,
    Event,
    InformationSystem,
    Map,
    Media,
    News,
    Policy,
    Project,
    Publication,
    Technology,
    TrainingSeminar,
    Webinar,
    Product,
    Tag,
)
from django import forms


class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CommodityForm, self).__init__(*args, **kwargs)
        self.fields["date_created"].required = False
        self.fields["commodity_img"].required = False
        self.fields["status"].required = False


# class AboutForm(forms.ModelForm):
#     class Meta:
#         model = About
#         fields = "__all__"


class AboutFooterForm(forms.ModelForm):
    class Meta:
        model = AboutFooter
        fields = "__all__"


class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = KnowledgeResources
        fields = ["knowledge_title", "knowledge_description"]


class CMIForm(forms.ModelForm):
    class Meta:
        model = CMI
        fields = [
            "cmi_name",
            "cmi_meaning",
            "cmi_description",
            "address",
            "contact_num",
            "email",
            "latitude",
            "longitude",
            "cmi_image",
            "url",
            "date_joined",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Making some fields optional
        for field in [
            "cmi_name",
            "cmi_meaning",
            "cmi_description",
            "address",
            "contact_num",
            "email",
            "latitude",
            "longitude",
            "url",
            "date_joined",
        ]:
            self.fields[field].required = False


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadVideo
        fields = "__all__"


class UsefulLinksForm(forms.ModelForm):
    class Meta:
        model = UsefulLinks
        fields = [
            "link_title",
            "link",
        ]

    def __init__(self, *args, **kwargs):
        super(UsefulLinksForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False


class ResourceMetadataForm(forms.ModelForm):
    """Form for the common metadata fields for all resource types."""

    class Meta:
        model = ResourceMetadata
        fields = ["title", "description", "resource_type", "is_approved", "is_featured"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter resource title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Provide a detailed description",
                }
            ),
            "resource_type": forms.Select(
                attrs={"class": "form-select", "onchange": "showResourceFields()"}
            ),
            "is_approved": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "start_date",
            "end_date",
            "location",
            "organizer",
            "event_file",
            "is_virtual",
        ]
        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event location"}
            ),
            "organizer": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter organizer name"}
            ),
            "event_file": forms.FileInput(attrs={"class": "form-control"}),
            "is_virtual": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class InformationSystemForm(forms.ModelForm):
    class Meta:
        model = InformationSystem
        fields = ["website_url", "system_owner", "last_updated"]
        widgets = {
            "website_url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "https://example.com"}
            ),
            "system_owner": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter system owner"}
            ),
            "last_updated": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ["map_file", "map_url", "latitude", "longitude"]
        widgets = {
            "map_file": forms.FileInput(attrs={"class": "form-control"}),
            "map_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/map",
                }
            ),
            "latitude": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.00000001"}
            ),
            "longitude": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.00000001"}
            ),
        }


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["media_type", "media_file", "media_url", "author"]
        widgets = {
            "media_type": forms.Select(attrs={"class": "form-select"}),
            "media_file": forms.FileInput(attrs={"class": "form-control"}),
            "media_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/media",
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter media author/creator",
                }
            ),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "publication_date",
            "source",
            "external_url",
            "content",
            "featured_image",
        ]
        widgets = {
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "source": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter news source"}
            ),
            "external_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/news",
                }
            ),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "featured_image": forms.FileInput(attrs={"class": "form-control"}),
        }


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = [
            "policy_number",
            "effective_date",
            "issuing_body",
            "policy_file",
            "policy_url",
            "status",
        ]
        widgets = {
            "policy_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter policy reference number",
                }
            ),
            "effective_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "issuing_body": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter issuing authority",
                }
            ),
            "policy_file": forms.FileInput(attrs={"class": "form-control"}),
            "policy_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/policy",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "start_date",
            "end_date",
            "budget",
            "funding_source",
            "project_lead",
            "contact_email",
            "status",
        ]
        widgets = {
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "budget": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "funding_source": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter funding source"}
            ),
            "project_lead": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter project lead name",
                }
            ),
            "contact_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter contact email"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = [
            "authors",
            "publication_date",
            "publisher",
            "doi",
            "isbn",
            "publication_type",
            "publication_file",
        ]
        widgets = {
            "authors": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Comma-separated list of authors",
                }
            ),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "publisher": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter publisher name"}
            ),
            "doi": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g., 10.1000/xyz123"}
            ),
            "isbn": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., 978-3-16-148410-0",
                }
            ),
            "publication_type": forms.Select(attrs={"class": "form-select"}),
            "publication_file": forms.FileInput(attrs={"class": "form-control"}),
        }


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ["developer", "release_date", "patent_number", "license_type"]
        widgets = {
            "developer": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter technology developer",
                }
            ),
            "release_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "patent_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter patent number if applicable",
                }
            ),
            "license_type": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter license type"}
            ),
        }


class TrainingSeminarForm(forms.ModelForm):
    class Meta:
        model = TrainingSeminar
        fields = ["start_date", "end_date", "location", "trainers", "target_audience"]
        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter training location",
                }
            ),
            "trainers": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "List of trainers/instructors",
                }
            ),
            "target_audience": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter target audience"}
            ),
        }


class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ["webinar_date", "duration_minutes", "platform", "presenters"]
        widgets = {
            "webinar_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "duration_minutes": forms.NumberInput(
                attrs={"class": "form-control", "min": 1}
            ),
            "platform": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., Zoom, Teams, etc.",
                }
            ),
            "presenters": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "List of presenters",
                }
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["manufacturer", "features", "technical_specifications", "price"]
        widgets = {
            "manufacturer": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter product manufacturer",
                }
            ),
            "features": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Key features of the product",
                }
            ),
            "technical_specifications": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Technical details",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "placeholder": "Price in PHP",
                }
            ),
        }


class CommoditySelectForm(forms.Form):
    """Form for selecting multiple commodities."""

    commodities = forms.ModelMultipleChoiceField(
        queryset=Commodity.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        required=False,
    )


class TagForm(forms.ModelForm):
    """Form for creating new tags."""

    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter tag name"}
            )
        }

from django import forms
from django import forms
from appAdmin.models import About

# Define icon choices outside Meta
ICON_CHOICES = [
    ('fas fa-heartbeat', 'Heartbeat'),
    ('fas fa-flask', 'Flask'),
    ('fas fa-lightbulb', 'Lightbulb'),
    ('fas fa-cogs', 'Cogs'),
    ('fas fa-seedling', 'Seedling'),
    ('fas fa-graduation-cap', 'Graduation Cap'),
    ('fas fa-rocket', 'Rocket'),
    ('fas fa-bolt', 'Bolt'),
    ('fas fa-chart-line', 'Chart Line'),
    ('fas fa-hands-helping', 'Helping Hands'),
]

class CommonFormStyle:
    common_textarea_attrs = {
        'class': 'form-control',
        'rows': 3,
        'style': 'min-height: 36px;',
    }

    common_input_attrs = {
        'class': 'form-control',
        'style': 'min-height: 36px;',
    }
# Define the AboutForm class with the custom widgets
from django import forms
from .models import (
    About,
    AboutRationale,
    AboutObjective,
    AboutObjectiveDetail,
    AboutActivity,
    AboutTimeline,
    AboutTeamMember,
    AboutTeamSocial,
)


# ✅ About Form
class AboutForm(forms.ModelForm, CommonFormStyle):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'project_name': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter project name...'}),
            # 'content': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter content...'}),
            'project_details': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter project details...'}),
            'project_rationale_desc': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter rationale...'}),
            # 'background_signature_desc': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter background and signature...'}),
            # 'project_objectives_desc': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter objectives...'}),
            # 'research_activities_desc': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter research activities...'}),
            # 'project_timeline_desc': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter timeline description...'}),
        }


# ✅ About Rationale Form
class AboutRationaleForm(forms.ModelForm, CommonFormStyle):
    # icon = forms.ChoiceField(
    #     choices=ICON_CHOICES,
    #     widget=forms.Select(attrs={**CommonFormStyle.common_input_attrs})
    # )

    class Meta:
        model = AboutRationale
        fields = ['about', 
        # 'icon', 
        'title', 'detail']
        widgets = {
            'about': forms.HiddenInput(),
            'title': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter title...'}),
            'detail': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter detail...'}),
        }

# ✅ About Objective Form
class AboutObjectiveForm(forms.ModelForm, CommonFormStyle):
    # icon = forms.ChoiceField(
    #     choices=ICON_CHOICES,
    #     widget=forms.Select(attrs={**CommonFormStyle.common_input_attrs})
    # )

    class Meta:
        model = AboutObjective
        fields = [
            'about', 
            # 'icon', 
            'title'
            # , 'detail'
            ]
        widgets = {
            'about': forms.HiddenInput(),
            'title': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter title...'}),
            # 'detail': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter detail...'}),
        }


# ✅ About Objective Detail Form
class AboutObjectiveDetailForm(forms.ModelForm, CommonFormStyle):
     

    class Meta:
        model = AboutObjectiveDetail
        fields = ['about', 'detail']
        widgets = {
            'about': forms.HiddenInput(),
            'detail': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter detail...'}),
        }


# ✅ About Activity Form
class AboutActivityForm(forms.ModelForm, CommonFormStyle):
    icon = forms.ChoiceField(
        choices=ICON_CHOICES,
        widget=forms.Select(attrs={**CommonFormStyle.common_input_attrs})
    )

    class Meta:
        model = AboutActivity
        fields = ['about', 'icon', 'title', 'detail']
        widgets = {
            'about': forms.HiddenInput(),
            'title': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter title...'}),
            'detail': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter detail...'}),
        }


# ✅ About Timeline Form
class AboutTimelineForm(forms.ModelForm, CommonFormStyle):

    class Meta:
        model = AboutTimeline
        fields = ['about', 
        # 'header', 
        'title', 'description']
        widgets = {
            'about': forms.HiddenInput(),
            # 'header': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter header...'}),
            'title': forms.TextInput(attrs={**CommonFormStyle.common_input_attrs, 'placeholder': 'Enter title...'}),
            'description': forms.Textarea(attrs={**CommonFormStyle.common_textarea_attrs, 'placeholder': 'Enter description...'}),
        }

# ✅ About Team Member Form

class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'


class AboutTeamMemberForm(forms.ModelForm):
    class Meta:
        model = AboutTeamMember
        fields = '__all__'
        widgets = {
            'about': forms.HiddenInput(),
            'profile_image': CustomClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name...'}),

            # 'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name...'}),
            # 'm_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter middle name...'}),
            # 'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name...'}),

            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter role...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email...'}),
        }

# ✅ About Team Social Form
SOCIAL_PLATFORM_CHOICES = [
    ('fab fa-facebook', 'Facebook'),
    ('fab fa-instagram', 'Instagram'),
    ('fab fa-tiktok', 'TikTok'),
    ('fab fa-twitter', 'Twitter'),
    ('fab fa-youtube', 'YouTube'),
    ('fab fa-github', 'GitHub'),
    ('fab fa-linkedin', 'LinkedIn'),
    ('fas fa-globe', 'Website'),
    ('fas fa-link', 'Other'),
]

class AboutTeamSocialForm(forms.ModelForm):
    platform = forms.ChoiceField(
        choices=SOCIAL_PLATFORM_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Platform"
    )

    class Meta:
        model = AboutTeamSocial
        fields = ['platform', 'link']
        widgets = {
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Profile Link'}),
        }