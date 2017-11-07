from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    # template_dir에 설정되어이있는 디렉토리를 찾음