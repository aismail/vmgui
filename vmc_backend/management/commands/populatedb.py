import os
import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core import management
from django.contrib.auth.management.commands import changepassword 
from vmc_backend.factories import *

from vmc_backend.models import Subject, Assignment, UsersToSubjects, Submission,\
    SubmissionComment
class Command(BaseCommand):

  def handle(self, *args, **options):
    #
    def deleteDB():
      print("temele")
      path = os.getcwd()
      pathToFile = path + "/vmc_backend/vmc_db"
      try:
        os.remove(pathToFile)
      except OSError:
        print 'Creating database'
    #run the syncdb
    def recreateDB():
      management.call_command('syncdb', interactive=False)

      # Creates the super user and sets his password.
      management.call_command('createsuperuser', interactive=False,
      username="cdl", email="cdl@gmail.com")
      command = changepassword.Command()
      command._get_pass = lambda *args: 'cdl'
      command.execute("cdl")


    def generateData(): 
      so = Subject(name = "Sisteme de operare",
       description = "Studentii vor invata conceptele din spatele sistemelor\
                     de operare", link = "")
      sd = Subject(name = "Structuri de date",
       description = "Studentii vor invata structuri de date de baza", link = "")
      pa = Subject(name = "Proiectarea algoritmilor",
       description = "Studentii vor fi introdusi in algoritmica", link = "")
      uso = Subject(name = "Utilizarea sistemelor de operare",
       description = "Studentii vor invata sa foloseasca Linux", link = "")
      pl = Subject(name = "Proiectare Logica",
       description = "Studentii vor invata proiectarea automatelor", link = "")
      ma = Subject(name = "Matematica 3",
       description = "Studentii vor invata transformate + probabilitati", link = "")
      ps = Subject(name = "Metode numerice",
       description = "Studentii vor invata diverse metode numerice.", link = "")
      mg = Subject(name = "Paradigme de programare",
       description = "Empty", link = "")
      pc = Subject(name = "Programarea calculatoarelor",
       description = "Studentii vor invata limbajul C", link = "")
      dc = Subject(name = "Logica", 
        description = "Empty", link = "")
      so.save()
      sd.save()
      pa.save()
      uso.save()
      pl.save()
      ma.save()
      ps.save()
      mg.save()
      pc.save()
      dc.save()
      print("obiectele sunt bune")

      soa = Assignment(subject = so, name = "SOTema1",
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      sob = Assignment(subject = so, name = "SOTema2", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      sda = Assignment(subject = sd, name = "SDTema1", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      sdb = Assignment(subject = sd, name = "SDTema3", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      paa = Assignment(subject = pa, name = "PATema3",
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      pab = Assignment(subject = pa, name = "PATema4",
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      usoa = Assignment(subject = uso, name = "USOTema4", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      usob = Assignment(subject = uso, name = "USOTema1", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      pla = Assignment(subject = pl, name = "PLTema5", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      plb = Assignment(subject = pl, name = "PLTema2", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      maa = Assignment(subject = ma, name = "MATema6", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      mab = Assignment(subject = ma, name = "MATema4", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      psa = Assignment(subject = ps, name = "PSTema7", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      psb = Assignment(subject = ps, name = "PSTema2", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      mga = Assignment(subject = mg, name = "MGTema8",
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      mgb = Assignment(subject = mg, name = "MGTema3",
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      pca = Assignment(subject = pc, name = "PCTema9", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      pcb = Assignment(subject = pc, name = "PCTema1", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      dca = Assignment(subject = dc, name = "DCTema10", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")

      dcb = Assignment(subject = dc, name = "DCTema11", 
        text = "Task1:Lorem ipsum dolor sit amet.\nTask2: consectetur\
                dipisicing elit\nTask3: sed do eiusmod tempor incididunt",
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")
      print("temele sunt bune")
      soa.save()
      sob.save()
      sda.save()
      sdb.save()
      paa.save()
      pab.save()
      usoa.save()
      usob.save()
      pla.save()
      plb.save()
      maa.save()
      mab.save()
      psa.save()
      psb.save()
      pca.save()
      pcb.save()
      dca.save()
      dcb.save()
      mga.save()
      mgb.save()

      user1 = User.objects.create_user('john', 'lennon@thebeatles.com',
       'password')
      user1.is_staff = False

      user2 = User.objects.create_user('Cosmin', 'lennon@thebeatles.com',
       'password')
      user2.is_staff = False

      user3 = User.objects.create_user('BogdanC', 'lennon@thebeatles.com',
       'password')
      user3.is_staff = False

      user4 = User.objects.create_user('BogdanB', 'lennon@thebeatles.com',
       'password')
      user4.is_staff = False

      user5 = User.objects.create_user('Andrei', 'lennon@thebeatles.com',
       'password')
      user5.is_staff = False

      user6 = User.objects.create_user('AndreiI', 'lennon@thebeatles.com',
       'password')
      user6.is_staff = False

      user7 = User.objects.create_user('Marius', 'lennon@thebeatles.com',
       'password')
      user7.is_staff = False

      user8 = User.objects.create_user('Vlad', 'lennon@thebeatles.com',
       'password')
      user8.is_staff = False

      user1.save()
      user2.save()
      user3.save()
      user4.save()
      user5.save()
      user6.save()
      user7.save()
      user8.save()

      right1 = UsersToSubjects( subject = so, user = user1, role = 'teacher')
      right2 = UsersToSubjects( subject = sd, user = user2, role = 'student')
      right3 = UsersToSubjects( subject = pa, user = user3, role = 'assistant')
      right4 = UsersToSubjects( subject = uso, user = user4, role = 'assistant')
      right5 = UsersToSubjects( subject = dc, user = user5, role = 'student')
      right6 = UsersToSubjects( subject = mg, user = user6, role = 'student')
      right7 = UsersToSubjects( subject = ma, user = user7, role = 'student')
      right8 = UsersToSubjects( subject = ps, user = user8, role = 'student')
      right9 = UsersToSubjects( subject = so, user = user2, role = 'assistant')
      right10 = UsersToSubjects( subject = so, user = user1, role = 'teacher')
      right11 = UsersToSubjects( subject = sd, user = user3, role = 'teacher')
      right12 = UsersToSubjects( subject = pa, user = user8, role = 'teacher')
      right13 = UsersToSubjects( subject = pa, user = user3, role = 'student')
      right14 = UsersToSubjects( subject = uso, user = user1, role = 'teacher')
      right15 = UsersToSubjects( subject = uso, user = user6, role = 'student')
      right16 = UsersToSubjects( subject = dc, user = user2, role = 'teacher')
      right17 = UsersToSubjects( subject = dc, user = user5, role = 'assistant')
      right18 = UsersToSubjects( subject = mg, user = user4, role = 'assistant')
      right19 = UsersToSubjects( subject = mg, user = user4, role = 'teacher')
      right20 = UsersToSubjects( subject = ma, user = user1, role = 'teacher')
      right21 = UsersToSubjects( subject = ma, user = user3, role = 'assistant')
      right22 = UsersToSubjects( subject = ps, user = user5, role = 'assistant')
      right23 = UsersToSubjects( subject = ps, user = user8, role = 'teacher')

      right1.save()
      right2.save()
      right3.save()
      right4.save()
      right5.save()
      right6.save()
      right7.save()
      right8.save()
      right9.save()
      right10.save()
      right11.save()
      right12.save()
      right13.save()
      right14.save()
      right15.save()
      right16.save()
      right17.save()
      right18.save()
      right19.save()
      right20.save()
      right21.save()
      right22.save()
      right23.save()

      submission1 = Submission(student = user2,assignment = sda)
      submission2 = Submission(student = user5,assignment = dca)
      submission3 = Submission(student = user6,assignment = mga)
      submission4 = Submission(student = user7,assignment = maa)
      submission5 = Submission(student = user8,assignment = psa)
      submission6 = Submission(student = user5,assignment = dca)
      submission7 = Submission(student = user6,assignment = mga)
      submission8 = Submission(student = user7,assignment = maa)
      submission9 = Submission(student = user7,assignment = sda)
      submission10 = Submission(student = user3,assignment = sda)
      submission11 = Submission(student = user3,assignment = dca)
      submission12 = Submission(student = user3,assignment = mga)
      submission13 = Submission(student = user2,assignment = maa)
      submission14 = Submission(student = user2,assignment = psa)
      submission15 = Submission(student = user7,assignment = sdb)
      submission16 = Submission(student = user5,assignment = dcb)
      submission17 = Submission(student = user6,assignment = mgb)
      submission18 = Submission(student = user7,assignment = mab)
      submission19 = Submission(student = user8,assignment = psb)
      submission20 = Submission(student = user5,assignment = dcb)
      submission21 = Submission(student = user6,assignment = mgb)
      submission22 = Submission(student = user7,assignment = mab)
      submission23 = Submission(student = user7,assignment = sdb)
      submission24 = Submission(student = user3,assignment = sdb)
      submission25 = Submission(student = user3,assignment = dcb)
      submission26 = Submission(student = user3,assignment = mgb)
      submission27 = Submission(student = user2,assignment = mab)
      submission28 = Submission(student = user2,assignment = psb)
      submission29 = Submission(student = user2,assignment = dcb)
      submission30 = Submission(student = user2,assignment = dca)

      submission1.save()
      submission2.save()
      submission3.save()
      submission4.save()
      submission5.save()
      submission6.save()
      submission7.save()
      submission8.save()
      submission9.save()
      submission10.save()
      submission11.save()
      submission12.save()
      submission13.save()
      submission14.save()
      submission15.save()
      submission16.save()
      submission17.save()
      submission18.save()
      submission19.save()
      submission20.save()
      submission21.save()
      submission22.save()
      submission23.save()
      submission24.save()
      submission25.save()
      submission26.save()
      submission27.save()
      submission28.save()
      submission29.save()
      submission30.save()

      comment1 = SubmissionComment(submission = submission1, comment = "test1")
      comment2 = SubmissionComment(submission = submission2, comment = "test2")
      comment3 = SubmissionComment(submission = submission3, comment = "test3")
      comment4 = SubmissionComment(submission = submission4, comment = "test4")
      comment5 = SubmissionComment(submission = submission5, comment = "test5")
      comment6 = SubmissionComment(submission = submission6, comment = "test6")
      comment7 = SubmissionComment(submission = submission7, comment = "test7")
      comment8 = SubmissionComment(submission = submission8, comment = "test8")

      comment1.save()
      comment2.save()
      comment3.save()
      comment4.save()
      comment5.save()
      comment6.save()
      comment7.save()
      comment8.save()
    deleteDB()
    recreateDB()
    generateData()

