define ['cs!widget'], (Widget) ->
    class AssignmentDetailsWidget extends Widget
        subscribed_channels: ['/assignments/{{id}}']
        template_name: 'templates/assignment_details_widget.hjs'

        get_assignments: (params) =>
            @renderLayout(assignment: params.model.toJSON(), false)
