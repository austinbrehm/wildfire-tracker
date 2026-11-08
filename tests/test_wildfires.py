from models.wildfires import WildfiresPage


def test_wildfires_page_navigation(page):
    wildfires_page = WildfiresPage(page)
    wildfires_page.navigate()
    assert page.url == wildfires_page.url


def test_wildfire_search(page):
    wildfires_page = WildfiresPage(page)
    wildfires_page.navigate()
    wildfires_page.state_textbox.fill("Colorado")
    wildfires_page.year_textbox.fill("2026")
    wildfires_page.search_button.click()
    assert wildfires_page.results_heading.is_visible()