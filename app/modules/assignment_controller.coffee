define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
           [subjects, assignments, submissions] = Utils.newDataChannels\
                ('/subjects', '/assignments', '/submissions')

           params =
                # Parameters passed to the assignment details widget.
                assignments_params:
                    'channels':
                        '/assignments': assignments
                    'id': @params.url_params[0]

                # Parameters passed to the breadcruds_widget.
                breadcrumbs_params:
                    'channels':
                        '/subjects': subjects
                        '/assignments': assignments
                        '/submissions': submissions

            @renderLayout(params)


