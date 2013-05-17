define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
           channel_params=
                '/submissions':
                    'assignment_id': this.url_params[0]
                '/assignments': {}
                '/subjects': {}

            [submissions, assignments, subjects] = Utils.newDataChannels(channel_params)

            params =
                # Parameters passed to the submissions list widget.
                submissions_list_params:
                    'channels':
                        '/submissions': submissions

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


