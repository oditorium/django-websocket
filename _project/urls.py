from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^ws/', include ('websock.urls')),
    url(r'^admin/', admin.site.urls),
]
