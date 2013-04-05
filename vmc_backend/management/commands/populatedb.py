import os
import factory
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
       description = "Empty", link = "")
      sd = Subject(name = "Structuri de date",
       description = "Empty", link = "")
      pa = Subject(name = "Proiectarea algoritmilor",
       description = "Empty", link = "")
      uso = Subject(name = "USO",
       description = "Empty", link = "")
      pl = Subject(name = "Proiectare Logica",
       description = "Empty", link = "")
      ma = Subject(name = "Matematica 3",
       description = "Empty", link = "")
      ps = Subject(name = "Piersica stricata",
       description = "Empty", link = "")
      mg = Subject(name = "Mar gaurit",
       description = "Empty", link = "")
      pc = Subject(name = "Programarea calculatoarelor",
       description = "Empty", link = "")
      dc = Subject(name = "Distrugerea calculatoarelor", 
        description = "Empty", link = "")
      so.save()
      sd.save()
      pa.save()
      uso.save()
      pl.save()
      ma.save()
      ps.save()
      pc.save()
      dc.save()
      mg.save()

      soa = Assignment(subject = so, name = "SOTema1", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      sda = Assignment(subject = sd, name = "SDTema2", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      paa = Assignment(subject = pa, name = "PATema3", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      usoa = Assignment(subject = uso, name = "USOTema4", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      pla = Assignment(subject = pl, name = "PLTema5", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      maa = Assignment(subject = ma, name = "MATema6", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      psa = Assignment(subject = ps, name = "PSTema7", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      mga = Assignment(subject = mg, name = "MGTema8", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      pca = Assignment(subject = pc, name = "PCTema9", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
      dca = Assignment(subject = dc, name = "DCTema10", text = "", 
        deadline = datetime.datetime.utcnow().replace(tzinfo=utc),
         attachments = "")  
    
      soa.save()
      sda.save()
      paa.save()
      usoa.save()
      pla.save()
      maa.save()
      psa.save()
      pca.save()
      dca.save()
      mga.save()

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

      right1.save()
      right2.save()
      right3.save()
      right4.save()
      right5.save()
      right6.save()
      right7.save()
      right8.save()

      submission1 = Submission(student = user2,assignment = sda)
      submission2 = Submission(student = user5,assignment = dca)
      submission3 = Submission(student = user6,assignment = mga)
      submission4 = Submission(student = user7,assignment = maa)
      submission5 = Submission(student = user8,assignment = psa)
      submission6 = Submission(student = user5,assignment = dca)
      submission7 = Submission(student = user6,assignment = mga)
      submission8 = Submission(student = user7,assignment = maa)

      submission1.save()
      submission2.save()
      submission3.save()
      submission4.save()
      submission5.save()
      submission6.save()
      submission7.save()
      submission8.save()

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

    generateData()
  
