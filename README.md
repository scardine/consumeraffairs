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
    *   Rating - [must be between 1 - 5](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L20)
    *   Title - [no more than 64 chars](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L24)
    *   Summary - [no more than 10k chars](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L27)
    *   IP Address - [IP of the review submitter](https://github.com/scardine/consumeraffairs/blob/master/reviews/views.py#L29)
    *   Submission date - the date the review was submitted
    *   Company - information about the company for which the review was submitted, can be simple text (e.g., name, company id, etc.) or a [separate model altogether](https://github.com/scardine/consumeraffairs/blob/master/reviews/models.py#L6)
    *   Reviewer Metadata - [information about the reviewer](https://github.com/scardine/consumeraffairs/blob/master/reviews/views.py#L24), can be simple text (e.g., name, email, reviewer id, etc.) or a separate model altogether
*   Unit tests must be included providing 100% code coverage
*   Include instructions on local setup details for both “app setup” and “data setup”

### Optional:

*   Provide an authenticated admin view that allows me to view review submissions
*   Document the API

Organize the schema and data models in whatever manner you think makes the most sense and feel free to add any additional style and flair to the project that you'd like.

# Development Environment Setup

## App Setup

Clone the repo:

    $ git clone https://github.com/scardine/consumeraffairs
    $ cd consumeraffairs
    
Create a virtual environment:

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    
Install dependencies:

    $ pip3 install -r requirements.txt


## Data Setup

Run migrations:

    $ python3 manage.py migrate
    
Create a super user:

    $ python3 manage.py createsuperuser
    
Optionally you can load some fake data created with Faker (this will create
a superuser root):

    $ python3 manage.py loaddata reviews/fixtures/fakedata.json
    $ python3 manage.py changepassword root
    
    
## Token authentication
    
For clients to authenticate, the token key should be included in the 
Authorization HTTP header. The key should be prefixed by the string literal "Token", 
with whitespace separating the two strings. For example:

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b    

You can create authentication tokens using the admin web interface. If
you want to create them in batch:

    $ python manage.py shell
    >>> from rest_framework.authtoken.models import Token
    >>> from reviews.models import *
    >>> User = get_user_model()
    >>> for u in User.objects.filter(auth_token=None): 
        print(u.username, Token.objects.create(user=u))
    >>> exit()

    
## Running the development webserver

Start a local server with:

    $ python3 manage.py runserver
    
The default address/port is http://localhost:8000/ - for more information
run:

    $ python3 manage.py help runserver
    
    
## Testing

In order to run tests:

    $ python3 manage.py test
    
    
    
## Support and Troubleshooting

Please email paulos at xtend.com.br with the problem description and/or 
screenshot/stacktrace and call +5511989634414.
 
I use Pycharm professional with Python 3.7 running on a Macbook pro. I
have not tested the instructions in other platforms, let me know if you 
find any problem - YMMV if you are using Linux or the Windows Subsystem 
for Linux - you may have to adapt the instructions if you are using 
Cygwin or GoW (or if you are brave enough to try to running this on Windows
without a posix shell). 