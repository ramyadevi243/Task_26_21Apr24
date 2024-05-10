import pytest
from pages import search_locator


# Used fixture from conftest file
@pytest.mark.usefixtures("driver")
def test_pagesearch(driver):
    # Created an instance for class IMDB_Search by importing search_locator
    test_search_instance = search_locator.IMDB_Search(driver)

    # Passed value for url
    url = "https://www.imdb.com/search/name/"

    # Calling all methods by importing search_locator from pages package
    test_search_instance.start(url)
    test_search_instance.scroll_window_down(300)
    test_search_instance.static_pause(1)
    test_search_instance.name_filter("Nolan")
    test_search_instance.scroll_window_down(300)
    test_search_instance.static_pause(1)
    test_search_instance.birth_date("30-07-1970")
    test_search_instance.scroll_window_down(300)
    test_search_instance.static_pause(1)
    test_search_instance.awards_recognition()
    test_search_instance.see_result()








