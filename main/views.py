from django.shortcuts import render, redirect
from django.views import generic
from .models import PageTitle, Course
from .models import Menu
from .forms import CreateForm
from django.urls import reverse
from .models import FooterInfo
from .models import Category
from .forms import OnlineOfferForm, StudentForm, TeacherForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import FeaturedCourses
from .models import AboutUs
from .models import PageCourses
from .models import PageNew
from .models import NewSidebar
from .models import PageContact
from django.views.generic import DetailView


# Create your views here.
def main(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Mistake'
    form = StudentForm()

    if request.method == 'POST':
        form1 = TeacherForm(request.POST)
        if form1.is_valid():
            form1.save()

    form1 = TeacherForm()

    menu_list = Menu.objects.all().order_by('order')
    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'categories': Category.objects.all(),
        'page': PageTitle.objects.all(),
        'featured_course': FeaturedCourses.objects.all(),
        'form': form,
        'form1': form1,
    }

    return render(request, 'main/index.html', context)


def courses(request):
    menu_list = Menu.objects.all().order_by('order')
    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'featured_course': FeaturedCourses.objects.all(),
        'pc_info': PageCourses.objects.all(),
        'page': PageTitle.objects.all(),

    }

    return render(request, 'main/courses.html', context)


def blog(request):
    menu_list = Menu.objects.all().order_by('order')
    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'page_news': PageNew.objects.all(),
        'page_side': NewSidebar.objects.all(),
        'page': PageTitle.objects.all(),
    }

    return render(request, 'main/blog.html', context)


def contact(request):
    menu_list = Menu.objects.all().order_by('order')

    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'side_info': FooterInfo.objects.last(),
        'p_contact': PageContact.objects.first(),
        'page': PageTitle.objects.all(),
    }

    return render(request, 'main/contact.html', context)


def about(request):
    menu_list = Menu.objects.all().order_by('order')
    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'about_info': AboutUs.objects.all(),
        'featured_course': FeaturedCourses.objects.all(),
        'page': PageTitle.objects.all(),
    }

    return render(request, 'main/about.html', context)


def log(request):
    menu_list = Menu.objects.all().order_by('order')
    context = {
        'menu_list': menu_list,
        'info': FooterInfo.objects.all(),
        'page': PageTitle.objects.all(),
    }

    return render(request, 'main/login.html', context)


class UserForm(generic.FormView):
    form_class = CreateForm
    template_name = 'main/login.html'

    def form_valid(self, form):
        form.save()
        return super(UserForm, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:success')


def success(request):
    return render(request, 'main/success.html')


def page_info(request):
    page = PageTitle.objects.all()
    return render(request, 'main/form.html', {'page': page})


class ContactPageView(generic.FormView):
    template_name = 'main/mail.html'
    form_class = OnlineOfferForm

    def get_success_url(self):
        return reverse('main:mail_url')

    def form_valid(self, form):
        send_mail('subject', 'message', 'sender@example.com', ['avaz243005@gmail.com'],
                  html_message='<b>Name: </b>' + form.cleaned_data.get('name') + '<br>' +
                               '<b>Subject: </b>' + form.cleaned_data.get('subject') + '<br>' +
                               '<b>Email: </b>' + form.cleaned_data.get('email') + '<br>' +
                               '<b>Message: </b>' + form.cleaned_data.get('message') + '<br>' +
                               '<b>Phone: </b>' + form.cleaned_data.get('phone') + '<br>'
                  )

        messages.add_message(self.request, messages.INFO, 'Thank you ! Your message has been sent.')
        return super().form_valid(form)


def service(request):
    a5 = Course.objects.all()
    return render(request, 'Shop/service.html', {'a5': a5})


class FooterCategory(DetailView):
    model = Course
    template_name = 'main/course_detail.html'
    context_object_name = 'foot_category'


class FeaturedDetail(DetailView):
    model = FeaturedCourses
    template_name = 'main/featured_courses.html'
    context_object_name = 'featured_courses'


class CourseCategory(DetailView):
    model = Category
    template_name = 'main/course_category.html'
    context_object_name = 'course_category'


class NewsDetail(DetailView):
    model = PageNew
    template_name = 'main/news_detail.html'
    context_object_name = 'news_detail'


