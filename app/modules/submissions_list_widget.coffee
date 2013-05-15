define ['cs!widget'], (Widget) ->
    class submissionsWidget extends Widget
        subscribed_channels: ['/submissions']
        template_name: 'templates/submissions_list_widget.hjs'


        get_submissions: (params) =>
            @renderLayout(submissions: params.collection.toJSON(), false)
