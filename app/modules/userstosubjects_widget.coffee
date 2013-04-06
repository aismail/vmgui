define ['cs!widget'], (Widget) ->
    class UserstosubjectsWidget extends Widget
        subscribed_channels: ['/subjects', '/userstosubjects']
        template_name: 'templates/userstosubjects_widget.hjs'

        agregated_channels:{get_userstosubjects_and_subjects: ['/subjects',\
                            '/userstosubjects']}
        get_userstosubjects_and_subjects: (subjects_params, userstosubjects_params) =>
            ###
                This method will be called whenever there are changes
                to the /todos channel. Changes can be of multiple types,
                as this data channel is actually a Backbone Collection.
                (There is another type of channel as well, which can store raw
                JSON data).
            ###
             @renderLayout(userstosubjects: userstosubjects_params.collection.toJSON(),false)

