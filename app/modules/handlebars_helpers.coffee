Handlebars.registerHelper 'user_to_subject_row', \
                                    (userstosubjects, subjects, options) ->
    buffer = ''
    for subject in subjects
        if userstosubjects.subject_id == subject.id
            buffer += "<td><a href=" + subject.link + ">" +
                subject.name + "</a></td><td>" + userstosubjects.role +
                "</td>"
            return new Handlebars.SafeString(buffer)
