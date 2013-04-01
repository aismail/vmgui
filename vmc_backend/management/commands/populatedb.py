import os
import factory
import datetime

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
              
    deleteDB()
    recreateDB()
    generateData()
  
