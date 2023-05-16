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
    - [Second page](#second-page)
    - [Third page](#third-page)
    - [Fourth page](#fourth-page)
    - [Logout](#logout)
  - [Structure](#structure)
    - [Logical Flow](#logical-flow)
    - [Features Left to Implement](#features-left-to-implement)
    - [Database design](#database-design)
  - [Technologies](#technologies)
  - [Testing](#testing)
    - [Functional Testing](#functional-testing)
    - [Pep8 Validation](#pep8-validation)
    - [Bugs and Fixes](#bugs-and-fixes)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
    - [Code](#code)

## Introduction

This is a booking system for a Recording Studio.
It contains of four (4) pages, a register/login option and a calender.
A Superuser is also created for full authority.

### Site Goals

- The purpose of the booking system is to simplify the actual booking.
- As a user be able to manage his/hers booking
- To make it easy for musicians to record both small ideas up to an entire album.

### Target Audience

- The audience of this booking system are musicians, both beginners and professionals.

### User Stories

- As a user, I would like to choose a day to book using a calender
- As a user, I would like to choose to have a technician to guide and help me
- As a user, I want to

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

## Testing

### Functional Testing

### Pep8 Validation

- Python syntax checker at [Extends class](https://extendsclass.com/python-tester.html) was used to check the code. No error was found.

### Bugs and Fixes

## Deployment

### Version Control

The site was created using the CodeAnywhere editor and pushed to github to the remote repository "??".

The following git commands were used throughout development to push code to the remote repo:

`git add .` - This command was used to add the file(s) to the staging area before they are committed.
`git commit -m "commit message"` - This command was used to commit changes to the local repository queue ready for the final step.
`git push` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The below steps were followed to deploy this project to Heroku:

## Credits

### Code

- I used Code Institutes walkthrough project as tutorial for setting everything up and get the connection to my Worksheet, and also for steps to deploy my program to Heroku.
