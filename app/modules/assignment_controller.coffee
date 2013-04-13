define ['cs!controller'], (Controller) ->
    class AssignmentController extends Controller
        action: =>
            # Create a new data channel holding the TODO list items.
            #
            # In a real world app, this channel will contain data fetched
            # from a RESTful API. In our toy application, data is taken
            # from fixture.js :) The channel configuration can be found in
            # datasource.js.
            #
            # In the variable "todos", we are storing a unique identifier
            # of the todos channel in the datasource.
            [submissions, assignments] = Utils.newDataChannels('/submissions',
                                        '/assignments')

            # We're using Handlebars.js for templating and in the template
            # associated with this controller (todo_page.hjs, configured in
            # urls.js) there are two widgets injected (with div class="uberwidget").
            # One is for the add task widget, and one for the task list widget.
            params =
                # Parameters passed to the TODO list widget.
                # It needs to have access to the todos channel in order to
                # display the items and treat events like new items added.
                submissions_params:
                    'channels':
                        '/submissions': submissions

            # Render the layout (todo_page.hjs)
            @renderLayout(params)

