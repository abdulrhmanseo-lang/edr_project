from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الجوال")

    def __str__(self):
        return self.name
