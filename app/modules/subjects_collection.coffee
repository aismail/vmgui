define ['cs!base_collection', 'cs!model/subject'], (BaseCollection, Subject) ->
    class SubjectCollection extends BaseCollection
        model: Subject

