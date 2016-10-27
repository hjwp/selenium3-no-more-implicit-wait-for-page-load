# selenium3-no-more-implicit-wait-for-page-load

Minimal repro showing selenium/geckodriver consistently showing stale element errors after clicking on a form submit (which does not happen for normal hyperlink clicks)

To run the repro:

    mkvirtualenv venvname
    pip install -r requirements.txt
    python tests.py
    
* See commit history if intereseted, can switch back to all hyperlinks, see test run to completion, consistently
* Can also switch back to Selenium 2 with a `pip install 'selenium<3'` and see it run to completion consistently with form submits (requires firefox 45 esr)
