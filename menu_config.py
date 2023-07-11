# menu_config.py
from st_pages import Page, Section, show_pages, add_page_title

def configure_menu():
    # Optional -- adds the title and icon to the current page
    add_page_title("Page Title Goes Here")

    # Specify what pages should be shown in the sidebar, and what their titles and icons should be
    show_pages(
        [
            Page("Home.py", "Home"),
            Section("Player"),
            Page("pages/Player/player_batting_season.py", "Batting"),
            Page("pages/Player/player_pitching_season.py", "Pitching"),
            Section("Team"),
            Section("References"),
            Page("pages/References/Data_Dictionary.py"),
        ]
    )

