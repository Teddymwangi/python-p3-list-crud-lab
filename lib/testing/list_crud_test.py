
import pytest
from lib.list_crud import *

def test_create_an_empty_list():
    assert create_an_empty_list() == []

def test_create_a_list():
    assert create_a_list() == [1, 2, 3, 4]

def test_add_element_to_end_of_list():
    assert add_element_to_end_of_list([1, 2, 3], 4) == [1, 2, 3, 4]

def test_add_element_to_start_of_list():
    assert add_element_to_start_of_list([2, 3, 4], 1) == [1, 2, 3, 4]

def test_remove_element_from_end_of_list():
    assert remove_element_from_end_of_list([1, 2, 3, 4]) == [1, 2, 3]

def test_remove_element_from_start_of_list():
    assert remove_element_from_start_of_list([1, 2, 3, 4]) == [2, 3, 4]

def test_retrieve_first_element_from_list():
    assert retrieve_first_element_from_list([1, 2, 3, 4]) == 1

def test_retrieve_element_from_index():
    assert retrieve_element_from_index([1, 2, 3, 4], 2) == 3

def test_retrieve_last_element_from_list():
    assert retrieve_last_element_from_list([1, 2, 3, 4]) == 4
