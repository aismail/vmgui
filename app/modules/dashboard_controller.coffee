define ['cs!controller'], (Controller) ->
    class DashboardController extends Controller
        action: =>
            # Create new data channels holding the Subjects and Usertosubjects
            # mapping. The channel configuration can be found in datasource.js.

            [subjects, userstosubjects] = Utils.newDataChannels('/subjects',
                                          '/userstosubjects')

            params =
                # Parameters passed to the Subjects list widget.
                list_params:
                    item_channels: 
                        '/items': userstosubjects
                        '/subjects': subjects
                    channels:
                        '/items': userstosubjects
                    item: 'userstosubjects'
                    item_element: 'tr'
                subjects_params:
                    'channels':
                        '/subjects': subjects

            # Render the layout (dashboard_controller.hjs)
            @renderLayout(params)

