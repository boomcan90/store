===============================
bookstore
===============================

An online book store for our Database module.
Project is based off this cookiecutter skeleton_.

.. _skeleton: https://github.com/sloria/cookiecutter-flask

Setup
----------

You will need to have ``node`` and ``npm`` installed and you will need to use npm to install ``bower``.
Instructions for `node and npm here`__. And for `bower here`__.

.. _nodenpm: https://docs.npmjs.com/getting-started/installing-node

__ nodenpm_

.. _bowerlink: https://bower.io/#install-bower

__ bowerlink_


If you are using Ubuntu:

You need to install python-dev and libpq-dev.

.. code-block :: bash

    sudo apt install libpq-dev python3-dev

If you are using pip3:

First, you need to install virtualenv_. This ensures that you only have the necessary
packages for this project. You don't want to pollute the global python "namespace"
with many libraries you might not need.

.. _virtualenv: https://virtualenv.pypa.io/en/stable/installation/

If you are using conda:

You just need to know how to create a virtual environment in conda for python.

Creation, activation and deactivation.

.. code-block :: bash

    conda create -n bookstore python
    source activate bookstore
    source deactivate

You will see something like this in terminal:

.. code-block :: bash

    (bookstore) robin-lee: <cursor>

Further instructions will be for conda.


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block :: bash

    export STORE_SECRET='something-really-secret'

Before running shell commands, set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables

.. code-block :: bash

    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment and ensure
that ``flask test`` runs smoothly. After activating the environment, check
that ``pip --version`` references the anaconda path for python.
Example:``pip 8.1.2 from /Users/robin/anaconda/envs/bookstore/lib/python3.5/site-packages (python 3.5)``

.. code-block :: bash

    git clone https://github.com/robin-lee/store
    cd store
    conda create -n bookstore python
    source activate bookstore
    pip install -r requirements/dev.txt
    bower install
    flask test
    flask run

You will see this for successful tests.

.. image:: doc_images/doc_test_success.png
    :width: 400


For a successful run, you will see a pretty welcome screen. Explore the various files and try to make sense of it.

.. image:: doc_images/doc_welcome_success.png
    :width: 400

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration.

.. code-block :: bash

    flask db init
    flask db migrate
    flask db upgrade
    flask run


Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.


Git Work Flow
----------

1. On Github, fork the orignal repository to create your own copy.
2. Go to your forked repository page and clone it to your local environment (e.g. Desktop). You should have done the setup in the ``Getting Started`` section. If you have not please make sure it works.

.. code-block :: bash

    git clone https://github.com/<your-username>/store
    cd store

3. Activate environment.

.. code-block :: bash

    source activate bookstore

4. Check that tests work.

.. code-block :: bash

    flask test

5. Now to ensure that git is setup properly. Run the command below and you should see that you have exactly one remote called origin. ("Remotes" are like nicknames for the URLs of repositories - origin is one, for example.)

.. code-block :: bash

     git remote

6. Add the original Github repository as a new remote and call it upstream. (Then try "git remote" again, you should now see two remotes listed.) When you cloned you cloned from your fork. Now we want to add the original (robin-lee) as a new remore so you can pull updates.

.. code-block :: bash

    git remote add upstream https://github.com/robin-lee/store.git
    git remote

7. To get updates. Check you are on YOUR master branch then fetch upstream.

.. code-block :: bash

    git checkout master
    git fetch upstream

8. Rewrite your master branch so that any commits of yours that aren't already in upstream/master are replayed on top of that other branch. This where there might be merge conflicts. You will want to always do this before starting work and before you make a pull-request.

.. code-block :: bash

    git rebase upstream/master

9. After you have made changes you can push changes to your fork.

.. code-block :: bash

    git add templates/newfile.html
    git add --all
    git commit -m "Added newfile that shows important stuff."
    git push origin master

10. Now you will want to submit a pull request to the repo. Make sure your project is synced with latest updates from the original repository. ENSURE TESTS RUN SUCCESSFULLY. If not fix it.

.. code-block :: bash

    git fetch upstream
    git rebase upstream/master
    flask test

11. Go to https://github.com/robin-lee/store/pulls and create new pull request.
12. You should see something like: "base fork: robin-lee/store, base: master; head fork: <you-user>/store, compare: master".
13. Confirm the code changes and create the pull request with a DESCRIPTIVE title and sensible comments.


