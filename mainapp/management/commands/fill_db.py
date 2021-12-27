import random
from uuid import uuid4
from django.core.management.base import BaseCommand, CommandError
from mainapp.models import User, Question
from mimesis import Person, Generic

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('users_quantity', type=int, help='Number of users to create')
        parser.add_argument('questions_quantity', type=int, help='Number of questions create')

    def handle(self, *args, **options):
        self.create_users(options['users_quantity'])
        self.create_questions(options['questions_quantity'])

    def create_users(self, quantity):
        _user = Person('ru')
        for i in range(quantity):
            user = User(uuid=uuid4(),
                first_name=_user.first_name(),
                last_name=_user.last_name())
            try:
                user.save()
            except Exception:
                raise CommandError(f'Cannot create user {user.first_name} {user.last_name}')
            else:
                self.stdout.write(self.style.SUCCESS(f'Succefully created {user.first_name} {user.last_name}'))


    def create_questions(self, quantity):
        _question = Generic('ru')
        users = User.objects.all()
        for i in range(quantity):
            current_user = random.choice(users)
            question = Question(creation_date=_question.datetime.date(start=2019, end=2021),
                                title=_question.text.title(),
                                is_answered=bool(round(random.random())),
                                link=_question.internet.url(),
                                author=current_user)
            try:
                question.save()
            except Exception:
                raise CommandError(f'Cannot create question {question.title[:15]}...')
            else:
                self.stdout.write(self.style.SUCCESS(f'Succesfully created {question.title[:15]}...'))