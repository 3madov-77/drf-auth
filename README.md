# Name of Peoject: ***Programing Stories API***

<br>

## Estimate of time needed to complete: ***5 h***

<br>

### Start time: ***12:30 am***
### Finish time: ***5:30 am***
### Actual time needed to complete: *** 4 h ***
### Version: ***1.0***


<br>
<hr>

# Notes:
full python server API, that uses 'Django' and 'REST API' framwork, with 'Token' Authentication & ready to Production..
it also conected with docker

- it had 5 main roots: 

    1. /admin:

        you can sign in and cheackout the users stories without the applity to edit them..

    2. api/v1/stories:

        watch all stories there in 'Json' format, or create new story.. (you need to be user)

    3. api/v1/stories/*story id:

        view specifec story and if you were the auther you can edit on or delete

    4. api/token/:

        get your access token & refresh token

    5. api/token/refresh:

        by passing your old token as body so it will retrun the refresh token..

<br>
<br>

***(this server support users and admin panell)***

***(this project fully coverd with tests for each function)***

***(you need to be user!)***