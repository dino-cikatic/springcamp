from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', 'Forme.apps.student.views.list_students', name='list_students'),
    url(r'^create_student/$', 'Forme.apps.student.views.create_student', name='create_student'),
    url(r'^create_student/(?P<id>([0-9]+))/$', 'Forme.apps.student.views.create_student', name='create_student'),
]