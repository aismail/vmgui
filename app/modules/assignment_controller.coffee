define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
           channel_params=
                '/submissions':
                    'assignment_id': this.url_params[0]
                '/assignments': {}

            [submissions, assignments] = Utils.newDataChannels(channel_params)

            params =
                # Parameters passed to the submissions list widget.
                submissions_list_params:
                    'channels':
                        '/submissions': submissions

            @renderLayout(params)


