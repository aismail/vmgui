define ['cs!widget'], (Widget) ->
    class SubjectDetailsWidget extends Widget
        subscribed_channels: ['/subjects/{{id}}']
        template_name: 'templates/subject_details_widget.hjs'

        get_subjects: (params) =>
            @renderLayout(subject: params.model.toJSON(), false)
