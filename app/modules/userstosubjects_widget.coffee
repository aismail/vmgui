define ['cs!widget'], (Widget) ->
    class UsertosubjectWidget extends Widget
        subscribed_channels: ['/subjects', '/userstosubjects']
        template_name: 'templates/usertosubject_widget.hjs'

        agregated_channels:{get_usertosubject_and_subjects: ['/subjects',\
                            '/userstosubjects']}
        get_usertosubject_and_subjects: (subjects_params, userstosubjects_params) =>
            ###
                This method will be called whenever there are changes
                to the /todos channel. Changes can be of multiple types,
                as this data channel is actually a Backbone Collection.
                (There is another type of channel as well, which can store raw
                JSON data).
            ###
             @renderLayout(usertosubject: usertosubject_params.collection.toJSON(),false)

