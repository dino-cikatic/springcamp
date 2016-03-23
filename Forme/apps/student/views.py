from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404

from Forme.apps.student.models import Student
from Forme.apps.student.forms import CreateStudentForm


def list_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {"students": students})


def create_student(request, id=None):
    student = Student.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = CreateStudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:list_students'))
    else:
        form = CreateStudentForm(instance=student)

    return render(request, 'create_student.html', {'form': form })