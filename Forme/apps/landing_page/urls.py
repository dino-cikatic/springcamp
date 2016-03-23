from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'Forme.apps.landing_page.views.landing_page', name='landing'),
]