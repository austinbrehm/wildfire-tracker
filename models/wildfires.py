from playwright.sync_api import Page


class WildfiresPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://wildfire-tracker-zeta-khaki.vercel.app/wildfires/"
        self.search_button = page.get_by_role("button", name="Search")
        self.results_heading = page.get_by_role("heading", name="Results")
        self.state_textbox = page.get_by_role("textbox", name="State")
        self.year_textbox = page.get_by_role("textbox", name="Year")

    def navigate(self):
        self.page.goto(self.url)
