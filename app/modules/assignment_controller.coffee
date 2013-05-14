define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
            [submissions] = Utils.newDataChannels('/submissions')

            params =
                # Parameters passed to the submissions list widget.
                submissions_params:
                    'channels':
                        '/submissions': submissions

            @renderLayout(params)


