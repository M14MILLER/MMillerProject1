import pytest


#utilized slack for help

from main import open_db, setup_db, add_college, get_data

def test_get_data():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?' \
            'school.degrees_awarded.predominant=2,3&fields=school.name,school.city,' \
            '2018.student.size,2017.student.size,' \
            '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,' \
            '2016.repayment.3_yr_repayment.overall'
    assert get_data(url) > 1000


#def test_add_college():
  #  conn, cursor
