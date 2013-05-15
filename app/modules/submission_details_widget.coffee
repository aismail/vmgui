define ['cs!widget'], (Widget) ->
    class SubmissionDetailsWidget extends Widget
        subscribed_channels: ['/submissions/{{id}}']
        template_name: 'templates/submission_details_widget.hjs'

        get_submission: (params) =>
            assignment_id = params.model.toJSON().assignment_id
            new_url = Utils.render_url(Utils.current_url()+"#assignments/{{id}}",\
                      {id:assignment_id}, [])
            params=
                submission: params.model.toJSON()
                url: new_url
            @renderLayout(params, false)
