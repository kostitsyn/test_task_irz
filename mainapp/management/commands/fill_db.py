import random
from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Question
from mimesis import Generic


class Command(BaseCommand):
    """
    Fill the database with test data.
    """
    def add_arguments(self, parser):
        parser.add_argument('questions_quantity', type=int, help='Number of questions create')

    def handle(self, *args, **options):
        self.create_questions(options['questions_quantity'])

    def create_questions(self, quantity):
        _question = Generic('ru')
        for i in range(quantity):
            question = Question(creation_date=_question.datetime.date(start=2019, end=2021),
                                title=_question.text.title(),
                                is_answered=bool(round(random.random())),
                                link=_question.internet.url(),
                                author=_question.person.full_name())
            try:
                question.save()
            except Exception:
                raise CommandError(f'Cannot create question {question.title[:15]}...')
            else:
                self.stdout.write(self.style.SUCCESS(f'Succesfully created {question.title[:15]}...'))