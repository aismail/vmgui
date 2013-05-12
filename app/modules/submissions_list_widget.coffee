define ['cs!widget'], (Widget) ->
    class submissionsWidget extends Widget
        subscribed_channels: ['/submissions']
        template_name: 'templates/submissions_list_widget.hjs'


        get_submissions: (submissions_params, subject_id) =>
            ###
            This method will be called whenever there are changes
            to the /todos channel. Changes can be of multiple types,
            as this data channel is actually a Backbone Collection.
            (There is another type of channel as well, which can store raw
            JSON data).
            ###
            params=
                submissions: submissions_params.collection.toJSON()

            @renderLayout(params,false)
