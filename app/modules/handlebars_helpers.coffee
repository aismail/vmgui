Handlebars.registerHelper 'user_to_subject_raw', \
                                    (userstosubjects, subjects, options) ->
    buffer = ''
    for subject in subjects
        if userstosubjects.subject_id == subject.id
            buffer += "<tr><td><a href=" + subject.link + ">" +
                subject.name + "</a></td><td>" + userstosubjects.role +
                "</td></tr>"
            return new Handlebars.SafeString(buffer)
