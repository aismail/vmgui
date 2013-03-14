from . import models
from django.contrib.auth.models import User
from django.utils.timezone import utc
import factory
import random
import datetime
from random import choice, randint


class UserFactory(factory.Factory):
    FACTORY_FOR = models.User
    username = factory.LazyAttribute(lambda x: '%030x' %
                                     random.randrange(256 ** 15))
    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))


class SubjectFactory(factory.Factory):
    FACTORY_FOR = models.Subject
    name = factory.LazyAttribute(lambda x: '%030x' %
                                 random.randrange(256 ** 15))
    description = factory.LazyAttribute(lambda x: '%055x' %
                                        random.randrange(256 ** 15))
    link = factory.Sequence(lambda n: 'www.numarul{0}emagic.com'.format(n))
    contact_person_email = factory.Sequence(lambda n:
                                            'user{0}@gmail.com'.format(n))


class AssignmentFactory(factory.Factory):
    FACTORY_FOR = models.Assignment
    subject_id = factory.SubFactory(SubjectFactory)
    name = factory.LazyAttribute(lambda x: '%030x' %
                                 random.randrange(256 ** 15))
    text = factory.LazyAttribute(lambda x: '%055x' %
                                 random.randrange(256 ** 15))
    deadline = datetime.datetime.utcnow().replace(tzinfo=utc)
    attachments = factory.Sequence(lambda n:
                                   'www.atasamente{0}.com'.format(n))


class UsersToSubjectsFactory(factory.Factory):
    FACTORY_FOR = models.UsersToSubjects
    subject_id = factory.SubFactory(SubjectFactory)
    user_id = factory.SubFactory(UserFactory)
    role = choice(['teacher', 'student', 'assistant'])


class SubmissionFactory(factory.Factory):
    FACTORY_FOR = models.Submission
    student_id = factory.SubFactory(UserFactory)
    assignment_id = factory.SubFactory(AssignmentFactory)
    uploaded_at = datetime.datetime.now()
    graded = choice([True, False])
    #TODO random filefield


class SubmissionCommentFactory(factory.Factory):
    FACTORY_FOR = models.SubmissionComment
    submission_id = factory.SubFactory(SubmissionFactory)
    filename = factory.LazyAttribute(lambda x: '%030x' %
                                     random.randrange(256 ** 15))
    line_no = randint(1, 100)
    comment = factory.LazyAttribute(lambda x: '%030x' %
                                    random.randrange(256 ** 15))
