import random
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

# Create your views here.
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequireMixin


class AgentListView(OrganisorAndLoginRequireMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganisorAndLoginRequireMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0,1000000)}")
        user.save()

        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile,
        )

        send_mail(
            subject="you are invited as Agent",
            message="you were added as agent on DJCRM. please come login to start working",
            from_email="admin@test.com",
            recipient_list=[user.email])

        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView (OrganisorAndLoginRequireMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(OrganisorAndLoginRequireMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    context_object_name = "agent"
    form_class = AgentModelForm

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteview(OrganisorAndLoginRequireMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
