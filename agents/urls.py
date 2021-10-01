from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteview


app_name = "agents"


urlpatterns = [
    path("", AgentListView.as_view(), name="agent-list"),
    path("agent-create", AgentCreateView.as_view(), name="agent-create"),
    path("<int:pk>/agent-detail", AgentDetailView.as_view(), name="agent-detail"),
    path("<int:pk>/agent-update", AgentUpdateView.as_view(), name="agent-update"),
    path("<int:pk>/agent-delete", AgentDeleteview.as_view(), name="agent-delete")

]
