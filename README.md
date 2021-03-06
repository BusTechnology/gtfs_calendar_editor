# GTFS Calendar Editor

[![Travis CI](https://api.travis-ci.org/willwong430/gtfs_calendar_app.png?style=badge)](https://travis-ci.org/willwong430/gtfs_calendar_app)

An intuitive web application built with a VueJS front-end and a Flask back-end to modify the GTFS calendar files.

## What is the purpose of the GTFS Calendar Editor?

Oftentimes, the GTFS has issues that stem from incorrect or missing service on a particular day. This tool gives the user an efficient and effective way to view, modify, and repackage the GTFS calendar files with the correct service for a date or a range of dates.  

## How do I use it?

1. Clone the repo

   `git clone https://github.com/BusTechnology/gtfs_calendar_app.git`

2. Go into the project directory

  `cd gtfs_calendar_app/`

3. Install dependencies if necessary

    a)  The PyPA recommended tool for installing Python packages.

      `apt install python-pip`

    b)  The npm package manager for JavaScript.

      `apt install npm`

4. `python setup.py` to install Python dependencies

5. ```cd gtfs_editor
      npm install
      cd .. ```

4. From command line, run the script to start up the app

   `./runserver`

5. The application will greet you on
   http://localhost:8080/

## Is it tested?

You betcha.  Run `python tests/calendar_tests.py` to see
the tests pass.
