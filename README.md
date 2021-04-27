# ddd_shop

The assessment is to build a virtual shop monitoring system:

The assessment should take you not more than 12 hours to finish but we are hoping for 8 hours.

IMPORTANT: Kindly clone the repo and use a different branch from master to submit your solution. once done, add us as a contributor.

## SCENARIO

Using the above cookiecutter template, please provide the following:

- Custom user system and include permissions. The various users to the system are as follows: Admin, Store Owner and Store Attendant.

- The Admin should be able to view data from all stores
- A store owner can have more than one store but the API endpoint should be able to show data of sales from each store on GET request from each days sales.
- A store attendant can only see data from the store they are assigned to
- The store attendant can upload data of sales for the day using a CSV or xlsx file (use provided template below) and the data stored in a database:

  ![alt text](https://github.com/Abilene-Paradox/ddd_assessment/blob/main/store_template.png)

- The store attendant can make changes to the uploaded data
- A store can have multiple attendants and the uploaded data should show the name of the attendant who uploads the file (above)
- A store owner can make a comment on the days sales
- An end point showing total sales of each item provided in the template per store only to the store owner

In addtition:

- The uploaded files are not processed in real time to allow corrections to be made in case of an error in the upload file.
- All files from all stores in the system are processed at the same time every day, let's assume its Kenya and all stores are closed by 1900Hrs and the processing happens at 2000Hrs, the process should be able to capture failures and re-run them.
- Once processed the files are moved into an archive directory but should be available to the store owner for download
- The system should also be able to check for file extensions to ensure only the right file extenssions can be uploaded

You can be as minimal as possible or detailed as possible, for any path chosen please comment your code.
We are looking at your problem solving skills and how well you can articulate your thought process.

If anything is unclear please feel free to reach out to us and we shall get back to you as soon as possible.

BEST OF LUCK.

License
: MIT

## Settings

Moved to
[settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out
  the form. Once you submit it, you'll see a "Verify Your E-mail
  Address" page. Go to your console to see a simulated email
  verification message. Copy the link into your browser. Now the
  user's email should be verified and ready to go.
- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy ddd_shop

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS
compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

```{.sourceCode .bash}
cd ddd_shop
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_
the celery commands are run. If you are in the same folder with
_manage.py_, you should be right.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

Custom Bootstrap Compilation \^\^\^\^\^\^

The generated CSS is set up with automatic Bootstrap recompilation with
variables of your choice. Bootstrap v4 is installed using npm and
customised by tweaking your variables in
`static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap
source](https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss),
or get explanations on them in the [Bootstrap
docs](https://getbootstrap.com/docs/4.1/getting-started/theming/).
