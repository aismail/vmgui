define ['cs!base_collection', 'cs!model/subject'], (BaseCollection, Assignment) ->
    class AssignmentCollection extends BaseCollection
        model: Assignment

