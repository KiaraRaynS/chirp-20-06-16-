from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from appdjango.models import Chirp, StopWord


class ViewIndex(ListView):
    template_name = 'index.html'
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount'] = Chirp.objects.all().count
        return context


class ChirpDetailView(DetailView):
    model = Chirp

    def get_queryset(self):
        return Chirp.objects.filter(user=self.request.user)


class CreateChirp(CreateView):
    model = Chirp
    fields = ['body']
    success_url = '/'

    def form_valid(self, form):
        stop_word = StopWord.objects.all()
        # if trump, clinton, sanders in chirp.body
        chirp_body = form.cleaned_data['body'].lower()
        for stop_word in stop_word:
            if stop_word.word in chirp_body:
                form.add_error('body', 'Please use elegant diction, not that')
                return self.form_invalid(form)
        chirp = form.save(commit=False)
        chirp.user = self.request.user
        return super().form_valid(form)
