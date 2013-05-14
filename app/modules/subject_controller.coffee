define ['cs!controller'], (Controller) ->
    class SubjectController extends Controller
        action: =>
            # Create a new data channel holding the Subjects items.
            [subjects] = Utils.newDataChannels('/subjects')

            params =
                # Parameters passed to the subject_details_widget.
                subjects_params:
                    'channels':
                        '/subjects': subjects

            # Render the layout (subject_controller.hjs)
            @renderLayout(params)

