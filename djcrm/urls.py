from leads import views
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view, name='landing_page'),
    path('leads/', include('leads.urls', namespace='lead',)),
]
