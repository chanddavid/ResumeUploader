
from django.shortcuts import redirect, render
from django.views import View
from .forms import ResumeForm
from .models import Resume
# Create your views here.


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')


class CandidateView(View):
    def get(self, request, pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html',{'candidate':candidate})
