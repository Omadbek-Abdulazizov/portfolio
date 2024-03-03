from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from portfolio_app.models import Portfolio, Skills, Slider,Category


# Create your views here.
class HomewView(View):
    def get(self, request):
        portfolio_data = Portfolio.objects.all()
        skills_data = Skills.objects.all()
        slider_data = Slider.objects.all()
        categories = Category.objects.all()

        context = {'portfolio_data': portfolio_data, 'skills_data': skills_data, 'slider_data': slider_data, 'categories': categories}
        return render(request, 'index.html', context)
    def post(self, request):
        f_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        recipient_list = [email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        context = {'f_name':f_name ,'email': email, 'subject': subject, 'message':message}
        return render(request, 'index.html', context)

def portfolio_filter(request,category_id):
    portfolio_data = Portfolio.objects.filter(category__id=category_id)
    skills_data = Skills.objects.all()
    slider_data = Slider.objects.all()
    categories = Category.objects.all()

    context = {'portfolio_data': portfolio_data, 'skills_data': skills_data, 'slider_data': slider_data, 'categories': categories}
    return render(request, 'index.html', context)
