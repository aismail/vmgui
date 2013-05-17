define ['cs!widget'], (Widget) ->
    class AssignmentsWidget extends Widget
        subscribed_channels: ['/assignments']
        template_name: 'templates/assignments_list_widget.hjs'


        get_assignments: (assignments_params) =>
            ###
                This method will be called whenever there are changes
                to the /assignments channel. Changes can be of multiple types,
                as this data channel is actually a Backbone Collection.
            ###
            params=
                url: Utils.render_url(Utils.current_url() + "#assignments/")
                assignments: assignments_params.collection.toJSON()

            @renderLayout(params,false)


