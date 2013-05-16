define ['cs!controller'], (Controller) ->
    class SubjectController extends Controller
        action: =>
            channel_params =
                '/subjects': {}
                '/assignments': 
                    'subject_id': this.url_params[0]

            [subjects, assignments] = Utils.newDataChannels(channel_params)

            params =
                # Parameters passed to the subject_details_widget.
                subjects_params:
                    'channels':
                        '/subjects': subjects
                    'id': @params.url_params[0]
                assignments_params:
                    'channels':
                        '/assignments': assignments

            # Render the layout (subject_controller.hjs)
            @renderLayout(params)

