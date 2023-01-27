from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_icon_css = '#__next > div.jss4 > div > div > div > ul:nth-child(2) > div:nth-child(1) > div.MuiListItemIcon-root > svg'
    main_page_button_xpath = '//ul[1]//div[1]/div[2]/span'
    players_button_xpath = '//ul[1]//div[2]/div/span'
    languages_button_xpath = '//*/ul[2]/div[1]'
    sign_out_button_xpath = '//*/ul[2]/div[2]'
    dev_team_contact_xpath = '//*/main/div[3]/div//div[3]/child::a'
    players_count_xpath = '//*/main/div[2]/div[1]/div'
    matches_count_xpath = '//*/main/div[2]/div[2]'
    reports_counts_xpath = '//*/main/div[2]/div[3]//div'
    event_count_xpath = '//*/main/div[2]/div[4]//div'
    add_player_button_xpath = '//div[2]//a/button'
    activity_xpath = '//main/div[3]/div[3]'

    pass
