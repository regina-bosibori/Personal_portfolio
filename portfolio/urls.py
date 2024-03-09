from django.contrib import admin
from django.urls import path
from myapp.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view()),
    path('admin/', admin.site.urls),
]
