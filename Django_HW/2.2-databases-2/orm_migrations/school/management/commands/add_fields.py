from django.core.management.base import BaseCommand, CommandError
from school.models import Teacher, Student, Student_Teachers


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for student in Student.objects.all():
            for teacher in Teacher.objects.all():
                new_teachers = Student_Teachers(student=student, teacher=teacher)
                new_teachers.save()

        self.stdout.write(self.style.SUCCESS('Successfully'))
