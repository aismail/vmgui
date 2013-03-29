import os
import factory

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
      for x in range(0, 10):
        SubjectFactory.create()
        AssignmentFactory.create()
        UsersToSubjectsFactory.create()
        SubmissionFactory.create()
        SubmissionCommentFactory.create()
        UserFactory.create()
    
    deleteDB()
    recreateDB()
    generateData()
  
