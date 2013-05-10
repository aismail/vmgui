define ['cs!widget'], (Widget) ->
    class UserstosubjectsWidget extends Widget
        subscribed_channels: ['/items/{{id}}', '/subjects']
        template_name: 'templates/userstosubjects_widget.hjs'

        aggregated_channels:{get_userstosubjects_and_subjects: ['/items/{{id}}',
                            '/subjects']}

        get_userstosubjects_and_subjects: (item_params, subjects_params) =>
            ###
                This method will be called whenever there are changes
                to the /todos channel. Changes can be of multiple types,
                as this data channel is actually a Backbone Collection.
                (There is another type of channel as well, which can store raw
                JSON data).
            ###
            subject_id = item_params.model.toJSON().subject_id
            params=
                item: item_params.model.toJSON()
                subject: subjects_params.collection.get(subject_id).toJSON()

            @renderLayout(params,false)

