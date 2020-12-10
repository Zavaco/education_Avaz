from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(null=True, max_length=50)
    password = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Student Info"
        verbose_name_plural = "Students Info"


class Category(models.Model):
    category_title = models.CharField(max_length=100, null=True)
    category_message = models.CharField(max_length=200, null=True)
    category_info = models.CharField(max_length=100, null=True)
    category_image = models.ImageField(null=True, blank=True)
    category_detail = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse('course_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Category Info"
        verbose_name_plural = "Categories Info"


class PageTitle(models.Model):
    slogan = models.CharField(max_length=100, null=True, blank=True)
    page_title = models.CharField(max_length=200, null=True)
    course_message = models.CharField(max_length=50, null=True)
    course_text = models.CharField(max_length=200, null=True)
    featured_title = models.CharField(max_length=50, null=True)
    featured_text = models.CharField(max_length=200, null=True)
    sign_up_title = models.CharField(max_length=50, null=True)
    sign_up_text = models.CharField(max_length=200, null=True)
    join_title = models.CharField(max_length=50, null=True)
    join_text = models.CharField(max_length=200, null=True)
    main_image = models.ImageField(null=True, blank=True)
    sign_up_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.page_title


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="name", null=True)
    to = models.CharField(max_length=50, verbose_name="to", default='', null=True)
    order = models.IntegerField(verbose_name="order")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    section_info = models.ForeignKey(PageTitle, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu_Item"
        verbose_name_plural = "Menu_Items"


class Course(models.Model):
    course_title = models.CharField(max_length=50, null=True)
    course_price = models.FloatField(null=True, blank=True)
    course_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    course_description = models.TextField(null=True, blank=True)
    course_menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "Course Info"
        verbose_name_plural = "Courses Info"


class UserRequest(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    user_phone = models.CharField(max_length=50, null=True)
    user_status = models.BooleanField(null=True, verbose_name='checked')
    request_message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "User_Request"
        verbose_name_plural = "User_Requests"


class FooterInfo(models.Model):
    footer_info = models.CharField(max_length=50, null=True)
    footer_info1 = models.CharField(max_length=50, null=True)
    footer_info2 = models.CharField(max_length=50, null=True)
    footer_category = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.footer_info


class FeaturedCourses(models.Model):
    fc_category = models.CharField(max_length=50, null=True, blank=True)
    fc_price = models.CharField(max_length=50, null=True)
    fc_image = models.ImageField(null=True)
    fc_message = models.CharField(max_length=150, null=True)
    fc_title = models.CharField(max_length=50, null=True)
    fc_info = models.CharField(max_length=50, null=True)
    fc_author_image = models.ImageField(null=True)
    fc_author_name = models.CharField(max_length=50, null=True)
    fc_author_position = models.CharField(max_length=50, null=True)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.fc_title

    def get_absolute_url(self):
        return reverse('featured_courses', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Featured_Course"
        verbose_name_plural = "Featured_Courses"


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, null=True)
    teacher_image = models.ImageField(null=True, blank=True)
    teacher_email = models.CharField(null=True, max_length=50)
    phone_number = models.IntegerField(null=True, blank=True)
    teacher_password = models.CharField(null=True, max_length=50)
    teacher_course = models.ForeignKey(FeaturedCourses, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
       return self.teacher_name

    class Meta:
        verbose_name = "Teacher Info"
        verbose_name_plural = "Teachers Info"


class AboutUs(models.Model):
    main_image = models.ImageField(null=True, blank=True)
    body_image = models.ImageField(null=True, blank=True)
    about_us_title = models.CharField(max_length=50, null=True)
    about_us_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.about_us_title


class PageCourses(models.Model):
    page_courses_img = models.ImageField(null=True, blank=True)
    page_courses_body_image = models.ImageField(null=True, blank=True)
    page_courses_price = models.CharField(max_length=50, null=True)
    pc_author_image = models.ImageField(null=True)
    pc_author_name = models.CharField(max_length=50, null=True)
    pc_author_position = models.CharField(max_length=50, null=True)
    pc_message = models.CharField(max_length=250, null=True)
    pc_title = models.CharField(max_length=50, null=True)
    pc_btn = models.CharField(max_length=50, null=True)
    pc_info = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.pc_title


class PageNew(models.Model):
    pn_main_image = models.ImageField(null=True, blank=True)
    pn_body_image = models.ImageField(null=True, blank=True)
    pn_body_title = models.CharField(max_length=50, null=True)
    pn_author_img = models.ImageField(null=True, blank=True)
    pn_author_name = models.CharField(max_length=50, null=True)
    pn_author_position = models.CharField(max_length=50, null=True)
    pn_author_date = models.CharField(max_length=50, null=True)
    pn_author_comment = models.CharField(max_length=50, null=True)
    pn_body_text = models.TextField(null=True, blank=True)
    pn_body_fulltext = models.TextField(null=True, blank=True)
    pn_body_btn = models.CharField(max_length=50, null=True)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.pn_body_title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})


class NewSidebar(models.Model):
    ns_categories = models.CharField(max_length=50, null=True, blank=True)
    ns_categories_info = models.CharField(max_length=50, null=True, blank=True)
    ns_month = models.CharField(max_length=50, null=True, blank=True)
    ns_month_info = models.CharField(max_length=50, null=True, blank=True)
    ns_archives = models.CharField(max_length=50, null=True, blank=True)
    ns_archives_info = models.CharField(max_length=50, null=True, blank=True)
    ns_img = models.ImageField(null=True, blank=True)
    news = models.ForeignKey(PageNew, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.ns_categories


class PageContact(models.Model):
    p_contact_bg = models.ImageField(null=True, blank=True)
    p_form_title = models.CharField(max_length=50, null=True)
    p_form_info = models.CharField(max_length=250, null=True)
    p_sidebar_title = models.CharField(max_length=50, null=True)
    p_sidebar_info = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.p_form_title











