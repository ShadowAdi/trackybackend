from django.urls import path
from .views import create,GetAllJobs,GetJobs,UpdateDeleteJob
urlpatterns = [
    path("Create/", view=create, name="Create"),
    path("All/", view=GetAllJobs, name="GetJobs"),
    path("Single/<int:pk>/", view=GetJobs, name="GetJob"),
        path("UpdateDelete/<int:pk>/", view=UpdateDeleteJob),

]
