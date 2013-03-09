from django.contrib import admin
from vmc_backend.models import Subject, Assignment, Submission, SubmissionComment, UsersToSubjects

admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(SubmissionComment)
admin.site.register(UsersToSubjects)
