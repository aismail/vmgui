define ['cs!widget'], (Widget) ->
    class submissionsWidget extends Widget
        subscribed_channels: ['/submissions']
        template_name: 'templates/submissions_list_widget.hjs'


        get_submissions: (params) =>
            url = Utils.current_url() + "#submissions/"
            params = 
                url: url
                submissions: params.collection.toJSON()
            @renderLayout(params, false)
