define ['cs!controller'], (Controller) ->
    class SubmissionController extends Controller
        action: =>
            # Create a new data channel holding the submissions.
            [submissions] = Utils.newDataChannels('/submissions')

            params =
                # Parameters passed to the submission_details_widget.
                # It needs to have access to the submissions channel in order to
                # display the details.
                submissions_params:
                    'channels':
                        '/submissions':submissions
            @renderLayout(params)

