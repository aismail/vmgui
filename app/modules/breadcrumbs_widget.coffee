define ['cs!widget'], (Widget) ->
    class BreadcrumbsWidget extends Widget
        subscribed_channels: ['/subjects', '/assignments','/submissions']
        template_name: 'templates/breadcrumbs_widget.hjs'

        aggregated_channels:{get_subjects_and_assignments: ['/subjects', '/assignments',
                                            '/submissions']}

        get_subjects_and_assignments: (subjects_params, assignments_params, submissions_params) =>
            base_url = Utils.current_url()
            output = [ {url:base_url, name: "Dashboard"}]
            current_url = window.location.href.split("/")
            id = current_url[current_url.length - 1]
            current_page = current_url[current_url.length - 2]
            current_page = current_page.substr(1)
            if current_page is "submissions"
                aux = submissions_params.collection.get(id)
                assignment_id = aux.attributes.assignment_id

            if assignment_id
                submission_id = id
                id = assignment_id

            if current_page is "assignments" or assignment_id
                assignment_id = id
                aux = assignments_params.collection.get(id)
                assignment = aux.attributes.name
                subject_id = aux.attributes.subject_id

            if current_page is "subjects"
                subject_id = id

            if subject_id
                aux = subjects_params.collection.get(subject_id)
                subject = aux.attributes.name

            if subject_id
                output.push({url: base_url + "#subjects/" + subject_id,name: subject})

            if assignment_id
                output.push({url: base_url + "#assignments/" + assignment_id,name: assignment})

            if submission_id
                output.push({url: base_url + "#submissions/" + submission_id,name: "Submission"})

            params=
                output: output
            @renderLayout(params, false)
