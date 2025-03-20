# filepath: c:\Users\mohid\todoproject\django-template\hello\urls.py
from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("log/", views.log_message, name="log"),
    path("edit/<int:pk>/", views.edit_message, name="edit_message"),
    path("delete/<int:pk>/", views.delete_message, name="delete_message"),
]