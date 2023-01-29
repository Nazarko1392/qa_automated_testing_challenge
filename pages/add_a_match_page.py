from pages.base_page import BasePage


class add_a_match_page(BasePage):
    matches_button_xpath = '//*/div[1]/ul[2]/div[2]'
    adding_match_form = '//*/div[1]/main'
    my_team_input_xpath = '//*/input[@name = "myTeam"]'
    enemy_team_input_xpath = '//*/input[@name = "enemyTeam"]'
    my_team_score_input_xpath = '//*/input[@name = "myTeamScore"]'
    enemy_team_score_input_xpath = '//*/input[@name = "enemyTeamScore"]'
    date_input_xpath = '//*/input[@name = "date"]'
    match_at_home_true_checkbox_xpath = '//*/input[@type ="radio"][@value="true"]'
    match_out_home_false_checkbox_xpath = '//*/input[@type = "radio"][@value="false"]'
    t_shirt_color_input_xpath = '//*/form//div[7]//div/input'
    league_input_xpath = '//*/form//div[8]//input'
    time_played_input_xpath = '//*/form//div[9]//input'
    number_input_xpath = '//*/input[@name = "number"]'
    web_match_input_xpath = '//*/input[@name = "webMatch"]'
    general_input_xpath = '//*/input[@name = "general"]'
    rating_input_xpath = '//*/input[@name = "rating"]'
    submit_button_xpath = '//*/button[@type = "submit"]'
    clear_button_xpath = '//*//div[3]/button[2]'


pass
