from django import forms

from website.models import Website, Snap


class WebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = ("title", "url", )


SnapFormset = forms.inlineformset_factory(Website, Snap, fields=("snap",), can_delete=True, extra=1)
