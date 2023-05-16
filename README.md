# Recording Studio Booking

## Table of contents

- [Recording Studio Booking](#recording-studio-booking)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Site Goals](#site-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [Existing Features](#existing-features)
      - [First page](#first-page)
        - [OPTION 1: Register](#option-1-register)
        - [OPTION 2: Login](#option-2-login)
        - [Admin](#admin)
    - [Second page](#second-page)
    - [Third page](#third-page)
    - [Fourth page](#fourth-page)
    - [Logout](#logout)
    - [Password reset](#password-reset)
    - [Remember me](#remember-me)
  - [Structure](#structure)
    - [Logical Flow](#logical-flow)
    - [Features Left to Implement](#features-left-to-implement)
    - [Database design](#database-design)
  - [Technologies](#technologies)
  - [Testing](#testing)
    - [Functional Testing](#functional-testing)
    - [Agile Methods](#agile-methods)
    - [Bugs and Fixes](#bugs-and-fixes)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
    - [Code](#code)
      - [Notes](#notes)

## Introduction

This is a booking system for a Recording Studio.
It contains of four (4) pages, a register/login option and a calender.
A Superuser is also created for full access.

### Site Goals

- The purpose of the booking system is to simplify the actual booking.
- As a user be able to manage his/hers booking
- To make it easy for musicians to record both small ideas up to an entire album.

### Target Audience

- The audience of this booking system are musicians, both beginners and professionals.

### User Stories

- As a user, I would like to choose a day to book using a calender
- As a user, I would like to choose to have a technician to guide and help me

### Existing Features

#### First page

- First when the site loads the user can register a new user or login if user already exists.

![firstpage](/static/assets/img/1.png)

- When a user is logged in, the "Login" switches to "Logout"

![firstpageLoggedin](/static/assets/img/11.png)

##### OPTION 1: Register

- Pressing the Register button will take the user to a Sign up-page.

![register](/static/assets/img/2.png)

- Username and Password has to be filled.

![registerPassw](/static/assets/img/3.png)

- Both fields for password has to be filled, otherwise it prompts the user to fill it and the user cannot sign up without typing it twise.

![registerPassw2](/static/assets/img/4.png)

- If the user enters different passwords, it shows a text that says "You must type the same password each time."

![registerPassw3](/static/assets/img/5.png)

##### OPTION 2: Login

- If the user already registered and has a username and password, press "Login"
- It will direct the user to a Sign in-view.

![login1](/static/assets/img/13.png)

- Username and Password are mandatory. If not entered signing in wont be possible and it will give a message about entering both fields.

![login2](/static/assets/img/14.png)

##### Admin

### Second page

- After the user have either registered a new user, or logged in by an already existing user, it loads the second page.
- It gives you a welcome message and a button that says "Book".
- The navbar switches from "Login" to "Logout" when a valid user is logged in.
- Pressing the button takes the user to the third page.

![secondpage](/static/assets/img/6.png)

### Third page

- At the third page a calender will appear.

![thirdpage1](/static/assets/img/7.png)

- If the small square to the right that looks like a calender is pressed a bigger window appears with the option to choose a date.

![thirdpage2](/static/assets/img/8.png)

- After a dates has been chosen, it will appear in the field.

![thirdpage3](/static/assets/img/9.png)

### Fourth page

- The last page appears after the user has pressed the button "SUBMIT" below the calender.
- This page confirms your booking, gives the user a "Thank you"-message and directs further questions to the email address in the footer.

![fourthpage](/static/assets/img/10.png)

### Logout

- When the user hits the Button "Logout", the app will ask again to confirm.

![logoutConfirm](/static/assets/img/12.png)

- After confirmation to logout, the user will be redirected to first page.

### Password reset

- If a user has forgotten his/hers password, the user can press the button of "Forgot password?" and will then be asked to enter a email address to be able to reset.

![passwReset](/static/assets/img/16.png)

### Remember me

- If a user doesn't wants to enter username or password more than once, there is a "Remember me"-checkbox.

![rememberMe](/static/assets/img/17.png)

## Structure

### Logical Flow

- I have created a flowchart of the structure for this app. Following flow is how the program works right now. See section of [Features left to Implement](#features-left-to-implement) for the expected final version.

![flowchart_current](/static/assets/img/actual_flowchart.png)

### Features Left to Implement

- This is a flowchart of the expected final version.

![flowchart_expected](/static/assets/img/exp_flowchart.png)

- Features to implement:

### Database design

## Technologies

- Python - Python was the main language to build this app.
- Bootstrap 5 was used for styling.
- Django was used as the framework for the entire project.
- Allauth was used to create the login-authorization
- Datepicker and Crispy forms was used to create the calender.
- GitHub - source code is hosted on GitHub.
- CodeAnywhere was used to develop this project.

## Testing

### Functional Testing
![test](/static/assets/img/test.png)

### Agile Methods
- I have used Agile methods to use as a guide through the project.

![agile](/static/assets/img/agile.png)


### Bugs and Fixes
- CSS is not loading properly
- For further info about bugs, check the Functional Testing.

## Deployment

### Version Control

The site was created using the CodeAnywhere editor and pushed to github to the remote repository "??".

The following git commands were used throughout development to push code to the remote repo:

`git add .` - This command was used to add the file(s) to the staging area before they are committed.
`git commit -m "commit message"` - This command was used to commit changes to the local repository queue ready for the final step.
`git push` - This command was used to push all committed code to the remote repository on github.


### Heroku Deployment

## Credits
* Credits to Tutor Support at Code Institute for guiding and assisting me when errors occurs, and helping me find a way forward.
  

### Code
* I used Code Institutes walkthrough project as tutorial for setting everything up and get the connection to my Worksheet, and also for steps to deploy my program to Heroku.
* For Allauth I used the lesson by Matt in "I Think therefore I blog"
* For the datepicker I used this tutorial at webpedia: https://webpedia.net/how-to-use-datepicker-in-django


#### Notes
- Secret data has been deployed to Github due to a mistake by me writing the URL in settings. For the deployed version this has been corrected, but still some commits has the sensitive information though.