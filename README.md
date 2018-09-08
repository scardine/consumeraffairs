# CA Code Challenge

### Backend Practical

Using Django, create a simple API that allows users to post and retrieve their reviews.

### Acceptance Criteria

*   The completed assignment must be hosted in a [git repository](https://github.com/scardine/consumeraffairs)
*   The repository must [include commit history (e.g., more than one commit)](https://github.com/scardine/consumeraffairs/commits/master)
*   Users are able to submit reviews to the API
*   Users are able to retrieve reviews that they submitted
*   Users [cannot see reviews submitted by other users](https://github.com/scardine/consumeraffairs/blob/master/reviews/views.py#L15)
*   Use of the API requires a unique auth token for each user
*   Submitted reviews must include, at least, the following attributes:
    *   Rating - [must be between 1 - 5](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L11)
    *   Title - [no more than 64 chars](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L17)
    *   Summary - [no more than 10k chars](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L18)
    *   IP Address - [IP of the review submitter](https://github.com/scardine/consumeraffairs/blob/master/reviews/views.py#L27)
    *   Submission date - the date the review was submitted
    *   Company - information about the company for which the review was submitted, can be simple text (e.g., name, company id, etc.) or a [separate model altogether](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L6)
    *   Reviewer Metadata - [information about the reviewer](https://github.com/scardine/consumeraffairs/blob/master/reviews/views.py#L27), can be simple text (e.g., name, email, reviewer id, etc.) or a separate model altogether
*   Unit tests must be included providing 100% code coverage
*   Include instructions on local setup details for both “app setup” and “data setup”

### Optional:

*   Provide an authenticated admin view that allows me to view review submissions
*   Document the API

Organize the schema and data models in whatever manner you think makes the most sense and feel free to add any additional style and flair to the project that you'd like.