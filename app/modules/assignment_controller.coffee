define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
           [assignments] = Utils.newDataChannels('/assignments')

           params =
                # Parameters passed to the assignment details widget.
                assignments_params:
                    'channels':
                        '/assignments': assignments
                    'id': @params.url_params[0]

            @renderLayout(params)


