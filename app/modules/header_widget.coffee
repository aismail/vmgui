define ['cs!widget'], (Widget) ->
    class HeaderWidget extends Widget
        template_name: 'templates/header_widget.hjs'

        initialize: =>
            ###
            Widget constructor - we only render the layout for now
            TODO: show the currently logged in user
            ###
            @renderLayout()

