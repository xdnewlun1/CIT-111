from names import make_full_name, extract_given_name, extract_family_name 
import pytest

#tests to see if it gets someones full name and show their last name first
def test_make_full_name():
    #last name first then first name
    assert make_full_name("Penelope", "Smith-Jones") == "Smith-Jones; Penelope"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("J","Lin-Bex") =="Lin-Bex; J"
    assert make_full_name("", "") == "; "

#get someones last name
def test_extract_family_name():
    assert extract_family_name ("Lee; Jenny") == "Lee"
    assert extract_family_name ("Lesbonessa; Jane")=="Lesbonessa"
    assert extract_family_name ("Lin-Bex; J")== "Lin-Bex"
    assert extract_family_name (" ; ") == " "

#tests to see if it gets someones first name
def test_extract_given_name():
    assert extract_given_name ("Lee; Jenny") == "Jenny"
    assert extract_given_name ("Lesbonessa; Jane")== "Jane"
    assert extract_given_name ("Lin-Bex; J")== "J"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "team/test_names.py"])
#python3 test_names.py