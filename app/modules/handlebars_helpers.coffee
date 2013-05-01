Handlebars.registerHelper 'user_to_subject_raw', \
                                    (userstosubjects, subjects, options) ->
    buffer = ''
    map = userstosubjects[1]
    for subject in subjects
        if map.subject_id == subject.id
            buffer += "<table><tr><td><a href=" + subject.link + ">" + 
                subject.name + "</a></td><td>" + map.role + "</td></tr></table>"
            return new Handlebars.SafeString(buffer)
