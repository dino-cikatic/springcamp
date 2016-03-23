from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def landing_page(request):
    return HttpResponseRedirect(reverse('student:list_students'))
