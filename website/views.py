from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from website.forms import WebsiteForm, SnapFormset
from website.models import Website


class WebsiteListView(ListView):
    context_object_name = "websites"
    template_name = "website/list.html"

    def get_queryset(self):
        queryset = Website.objects.actives()
        return queryset


class WebsiteDetailView(DetailView):
    model = Website
    template_name = "website/detail.html"


class WebsiteCreateView(LoginRequiredMixin, CreateView):
    model = Website
    template_name: str = "website/create.html"
    form_class = WebsiteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = SnapFormset(self.request.POST or None, files=self.request.FILES or None)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context["formset"]
        if formset.is_valid():
            print(formset)
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)
