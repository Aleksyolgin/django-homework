from django.shortcuts import render
from django.views.generic import FormView

from forms.forms import UserForm


class Forms(FormView):
    form_class = UserForm
    template_name = 'index.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


def thanks(request):
    return render(request, 'thanks.html')
