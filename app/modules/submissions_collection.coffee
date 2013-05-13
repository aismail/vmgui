define ['cs!base_collection', 'cs!model/submission'], (BaseCollection, Submission) ->
    class SubmissionCollection extends BaseCollection
        model: Submission

