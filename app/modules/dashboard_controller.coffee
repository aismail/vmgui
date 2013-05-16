define ['cs!controller'], (Controller) ->
    class DashboardController extends Controller
        action: =>
            # Create new data channels holding the Subjects and Usertosubjects
            # mapping. The channel configuration can be found in datasource.js.

            [subjects, assignments, submissions, userstosubjects] = \
                Utils.newDataChannels('/subjects', '/assignments', '/submissions',
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
                breadcrumbs_params:
                    'channels':
                        '/subjects': subjects
                        '/assignments': assignments
                        '/submissions': submissions

            # Render the layout (dashboard_controller.hjs)
            @renderLayout(params)

