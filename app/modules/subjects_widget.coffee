define ['cs!widget'], (Widget) ->
    class SubjectsWidget extends Widget
        subscribed_channels: ['/subjects']
        template_name: 'templates/subjects_widget.hjs'

        get_subjects: (params) =>
            ###
                This method will be called whenever there are changes
                to the /todos channel. Changes can be of multiple types,
                as this data channel is actually a Backbone Collection.
                (There is another type of channel as well, which can store raw
                JSON data).
            ###
            if params.type is 'reset'
                @renderLayout(subjects: params.collection.toJSON(), false)

