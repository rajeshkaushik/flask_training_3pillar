# flask_training_3pillar
Flask training project for python workshop at 3pillar
Running tests
    pytest .

Running flake8 for static code analysis
    flake8 .

Checking test coverage report

    coverage run -m pytest && coverage report --omit='*lib/*.py,tests/*.py'
