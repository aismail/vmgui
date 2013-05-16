define ['cs!controller'], (Controller) ->
    class SubmissionController extends Controller
        action: =>
            # Create a new data channel holding the submissions.
            [subjects, assignments, submissions] = Utils.newDataChannels\
                ('/subjects', '/assignments', '/submissions')

            params =
                # Parameters passed to the submission_details_widget.
                # It needs to have access to the submissions channel in order to
                # display the details.
                submissions_params:
                    'channels':
                        '/submissions':submissions
                    'id': @params.url_params[0]

                # Parameters passed to the breadcruds_widget.
                breadcrumbs_params:
                    'channels':
                        '/subjects': subjects
                        '/assignments': assignments
                        '/submissions': submissions
            @renderLayout(params)

