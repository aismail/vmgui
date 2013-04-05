import random
import datetime
import factory
from tempfile import NamedTemporaryFile

from django.utils.timezone import utc
from django.core.files import File

from . import models

def generateFile():
    new_file = NamedTemporaryFile(delete=False)
    new_file.write("Some content")
    return new_file.name


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


class AssignmentFactory(factory.Factory):
    FACTORY_FOR = models.Assignment
    subject = factory.SubFactory(SubjectFactory)
    name = factory.LazyAttribute(lambda x: '%030x' %
                                 random.randrange(256 ** 15))
    text = factory.LazyAttribute(lambda x: '%055x' %
                                 random.randrange(256 ** 15))
    deadline = datetime.datetime.utcnow().replace(tzinfo=utc)
    attachments = factory.Sequence(lambda n:
                                   'www.atasamente{0}.com'.format(n))


class UsersToSubjectsFactory(factory.Factory):
    FACTORY_FOR = models.UsersToSubjects
    subject = factory.SubFactory(SubjectFactory)
    user = factory.SubFactory(UserFactory)
    role = random.choice(['teacher', 'student', 'assistant'])


class SubmissionFactory(factory.Factory):
    FACTORY_FOR = models.Submission
    student = factory.SubFactory(UserFactory)
    assignment = factory.SubFactory(AssignmentFactory)
    uploaded_at = datetime.datetime.now()
    graded = random.choice([True, False])
    content = File(open(generateFile()))


class SubmissionCommentFactory(factory.Factory):
    FACTORY_FOR = models.SubmissionComment
    submission = factory.SubFactory(SubmissionFactory)
    filename = factory.LazyAttribute(lambda x: '%030x' %
                                     random.randrange(256 ** 15))
    line_no = random.randint(1, 100)
    comment = factory.LazyAttribute(lambda x: '%030x' %
                                    random.randrange(256 ** 15))
