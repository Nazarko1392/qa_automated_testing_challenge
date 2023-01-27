# Task 1: Software configuration.
## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

>   Hello! My name is **[Nazar](https://www.instagram.com/nazarko1392/)**. 
    I'm a **Manual Quality Assurance** engineer.
    Recently, I began to think about starting to study **Automated Testing**.
    I believe that I'm lucky coz I saw an ad for your courses on Instagram.
    I'm located in Poland and this is a chance to get the necessary basic knowledge of test automation, improve my skills, 
    set up communication with new people and get an interview at a Polish IT company.
    With best regards!



![](https://www.metaltoad.com/sites/default/files/styles/large_personal_photo_870x500_/public/2021-01/quality-assurance_1.jpg?itok=YwEP6R-o)

# Task 2: Selectors.
## Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.

| Element | **Login** _XPath selectors_       |
|---------|:----------------------------------|
|         |
| 1       | //input[@id='login']              |
| 2       | //*[@id='login' or @name='login'] |
| 3       | //div/input[@type='text']         |

| Element | **Password** _XPath selectors_     |
|:--------|------------------------------------|
|         |
| 1       | //label[@for='password']           |
| 2       | //div/label[@id='password-label']  |
| 3       | //div/child::input[@id='password'] |

| Element | **Language** _XPath selectors_             |
|:--------|--------------------------------------------|
|         |
| 1       | //*/form/div/div[2]/div                    |
| 2       | //ul[@role='listbox']                      |
| 3       | //ul[@role='listbox']/li[@data-value='pl'] |


| Element | **Sign In** _XPath selectors_                                                         |
|:--------|---------------------------------------------------------------------------------------|
|         |
| 1       | //button[@type='submit']/span[contains(text(),'Sign in') or @class='MuiButton-label'] |
| 2       | //*[@tabindex='0' and @type='submit']                                                 |
| 3       | //span[@class='MuiTouchRipple-root']                                                  |