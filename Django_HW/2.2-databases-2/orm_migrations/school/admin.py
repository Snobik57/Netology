from django.contrib import admin

from .models import Student, Teacher, Student_Teachers


class Student_TeachersInline(admin.StackedInline):
    model = Student_Teachers
    extra = 3


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['name', 'group']
    inlines = [Student_TeachersInline,]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['name', 'subject']