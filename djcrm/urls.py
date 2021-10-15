from django.conf import settings
from django.conf.urls.static import static
from leads import views
from django.contrib import admin
from django.urls import path, include
from leads.views import  LandingView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='landing_page'),
    path('leads/', include('leads.urls', namespace='lead',)),
]


#if settings.DEBUG:
 #   urlpatterns += [
  #      static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
   # ]