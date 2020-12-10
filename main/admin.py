from django.contrib import admin
from .models import Student
from .models import Menu
from .models import Teacher
from .models import Course
from .models import Category
from .models import UserRequest
from .models import PageTitle
from .models import FooterInfo
from .models import FeaturedCourses
from .models import AboutUs
from .models import PageCourses
from .models import PageNew
from .models import NewSidebar
from .models import PageContact


class UserRequestAdmin(admin.ModelAdmin):
   list_display = ('user_phone', 'user_name')
   list_filter = ('user_status',)


# Register your models here.
admin.site.register(Student)
admin.site.register(Menu)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(UserRequest, UserRequestAdmin)
admin.site.register(PageTitle)
admin.site.register(FooterInfo)
admin.site.register(FeaturedCourses)
admin.site.register(AboutUs)
admin.site.register(PageCourses)
admin.site.register(PageNew)
admin.site.register(NewSidebar)
admin.site.register(PageContact)




