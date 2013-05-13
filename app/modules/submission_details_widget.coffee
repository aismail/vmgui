define ['cs!widget'], (Widget) ->
    class SubmissionDetailsWidget extends Widget
        subscribed_channels: ['/submissions/{{id}}']
        template_name: 'templates/submissions_details_widget.hjs'

        get_submission: (params) =>
            @renderLayout(submission: params.model.toJSON(), false)
