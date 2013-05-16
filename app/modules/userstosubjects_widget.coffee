define ['cs!widget'], (Widget) ->
    class UserstosubjectsWidget extends Widget
        subscribed_channels: ['/items/{{id}}', '/subjects']
        template_name: 'templates/userstosubjects_widget.hjs'

        aggregated_channels:{get_userstosubjects_and_subjects: ['/items/{{id}}',
                            '/subjects']}

        get_userstosubjects_and_subjects: (item_params, subjects_params) =>
            ###
                This method will be called whenever there are changes
                to the /subjects channel or to the /userstosubjects channel.
            ###
            subject_id = item_params.model.toJSON().subject_id
            new_url = Utils.render_url(Utils.current_url() + "#subjects/{{id}}",\
                      {id: subject_id}, [])
            params=
                item: item_params.model.toJSON()
                subject: subjects_params.collection.get(subject_id).toJSON()
                url: new_url

            @renderLayout(params,false)

