# Dorsia Restaurant
![Screenshot of a am I responsive](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680042938/Dorsia%20PP4%20Images/Readme/am_i_responsive_ggcsod.jpg)

[Live application can be found here](https://pp4-dorsia-restaurant.herokuapp.com/)

This is a full-stack framework project. It was built using Django, Python, JavaScript, Bootstrap, HTML and CSS. This is a restaurant website featuring the menu of the Dorsia Restaurant from Bret Easton Ellis' book [American Psycho](https://en.wikipedia.org/wiki/American_Psycho). The website is meant to display the menu to the customers and allow them to make,edit and delete their own reservations.

<hr>

## User Experience

The target audience for the restaurant:
- Affluent individuals
- Food enthusiasts
- Business professionals
- Special occasion dinners

Overall the target audience would be individuals willing to pay a premium price for a high-end dining experience.

The users are presented with:
- A website that is concise and easy to navigate
- Menus that offer information about every meal
- The ability to make a user account to make or edit a reservation
- Forms to make or edit a reservation

The website offers a responsive design and allows for intuitive navigation.

## User Stories
All my User Stories for this project with their acceptance criteria and tasks can be found [here](https://github.com/users/SamSswi/projects/5)

1. As an Admin I can log in as a super user so that I can access the backend of the website

2. As an Admin I can make changes to the menu items so that the users sees an up-to-date menu

3. As a User I can view detailed info about the items in the menu so that I have a better familiarity with the particularities of each meal served

4. As a User I can view the items in the restaurant menu in a clear way so that I know beforehand what dishes and drinks are served, and can get familiar with the menu of the restaurant

5. As a User I can easily and intuitively navigate the website so that I can view the content I am interested in

6. As a user I can Log In or Sign Up with email and password so that I can create an account and enjoy the services of the restaurant

7. As a User I can make a reservation at the restaurant so that I can enjoy the foods, drinks, and services of this restaurant

8. As a User I can View and Edit my bookings so that I can personally manage my reservations without contacting the restaurant

9. As a User I can access a front-end interface that meets accessibility guidelines and follows the principles of UX design so that I can interact with the web application in an intuitive and easy-to-use way

10. As a User I can see the key information on the home page so that I won't have to search for it

11. As a User I can Sign Up with a social media account so that the necessary information is auto-filled

12. As a User I can have suitable information about potential allergens in the menu items so that the health and safety of me and my guests are preserved

13. As a User I can contact the restaurant so that I can receive information I am interested in, and communicate important information to the restaurant administration

14. As a Logged In User I can edit my personal information so that the information I use for future bookings is updated and my privacy is safe

## Scope
To achieve the desired goals, the following features are included:
- Responsive navigation bar to allow navigation to most pages of the website
- Landing page with information about the restaurant and buttons for menu and making a reservation.
- Menu page with the food and drinks menu
- Make a reservation page, where the logged-in users have access to a booking form to make a reservation.
- Manage Reservations page, where logged-in users can read, edit and delete their reservations.
- Edit reservation page, where the logged-in users can edit the details of one of their reservations.
- Delete reservation page, where the logged-in users who pushed the delete button on a reservation can review and take decisive action on it.

## Database
The website requires a database to function and store information. I built three custom models for that and used the built-in User model for user authentication.

The three custom models are Booking, Meal, and Drink. The Booking model allows the logged-in user to make a reservation. The Meal and Drink models help the admin update the menu from the backend without editing the website code.

In the Relationship Diagram below, it can be seen how the models relate to each other.

![Relationship Diagram](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680040304/Dorsia%20PP4%20Images/Readme/DatabaseTables_xq8xes.jpg)

## Wireframes
[The Wireframes can be viewed here.](/WIREFRAMES.md)

Note: The actual website can differ from the original wireframes.

## Colors
The colors I chose for this website are a shade of bone (##E3DAC9) and a warm gray (#6E7178) with subtle variations. It is not designed to be an attention-grabbing color combination, but it is supposed to suggest warmth and elegance. 

# Features

## Navigation bar
The navigation bar contains links to all the relevant active pages. The Edit Reservation and Delete Reservation pages can be accessed from the Manage Reservations page, as they require a booking_id to know what reservation to act upon.

If the user is logged in, the right side of the Navigation Bar displays the following links: "Manage Reservations" and "Log Out".
![Screenshot of the navigation bar initial](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680047949/Dorsia%20PP4%20Images/Readme/navigation_bar_logged_out_buvbgi.jpg)

If the user is not logged in, then the options on the right side of the Navigation bar are to log in or register.
![Screenshot of the navigation bar logged-in user](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680047949/Dorsia%20PP4%20Images/Readme/navigation_bar_logged-in_ham8ku.jpg)

The navigation bar is responsive and collapses on smaller screens.

![Screenshot of the navigation bar collapsed](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680047949/Dorsia%20PP4%20Images/Readme/navigation_bar_collapsed_ow4nar.jpg)


## Home page
The home page features a landing area (where the name "Dorsia" is displayed), a bar with buttons allowing the user to access the menu or make a reservation, and an About Us section with a brief description of the restaurant.
![Screenshot of the home page](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680048603/Dorsia%20PP4%20Images/Readme/home_page_tbg2b3.jpg)

## Menu
The menu page displays separately the sections of the menu. Each item has a name and a description. The menu items can be added, edited or deleted by the admin in the backend.
![Screenshot of the menu page](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680048735/Dorsia%20PP4%20Images/Readme/menu_page_frruof.jpg)

## Make a Reservation
This page can be accessed only by the logged-in users. The visitors who are not registered yet, are redirected to the Sign Up page.
The page conatins a form the user can fill. The fields are not pre-populated.
![Screenshot of the make a reservation page](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680048862/Dorsia%20PP4%20Images/Readme/make_a_reservation_page_vzrctz.jpg)

## Manage Reservations
The link to this page is displayed in the navbar to the logged in users. This page shows the user a list of the reservations they have previously made, and offers them the opportunity to Edit or Delete the reservations that have not expired or are not less than one day away from the current date.
This reservation is made for a future date so the user can still edit it:
![Screenshot of the manage reservations page future](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049252/Dorsia%20PP4%20Images/Readme/manage_reservations_page_future_ujskga.jpg)
The following reservation cannot be edited anymore by the user. In case the user wants to modify it or cancel it, they should contact the restaurant.
![Screenshot of the manage reservations page past](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049446/Dorsia%20PP4%20Images/Readme/manage_reservations_page_past_oua9j0.jpg)

## Edit Reservation
This page displays the reservation form pre-populated using booking_id the user is able to change any piece of information they want and submit it. After submitting the form they're redirected to the Manage Reservations page where they can view the updated reservation.

![Screenshot of the edit reservation page](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049598/Dorsia%20PP4%20Images/Readme/edit_reservation_page_oyyxzu.jpg)

## Delete Reservation
This page displays information about the reservation the user chose to delete and gives them a chance to change their mind before definitively canceling their reservation.
![Screenshot of the delete reservation page](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049724/Dorsia%20PP4%20Images/Readme/delete_reservation_page_hwlezy.jpg)

## Footer
The footer displays some key information about the restaurant. It has two sections. The first section is the 'Opening Hours' and the second section displays the address, contact information and social media links.
![Screenshot of the footer](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049804/Dorsia%20PP4%20Images/Readme/footer_vaqcp7.jpg)
<hr>
<br>

# Technologies Used
- Python - the core programming language
- Django - the Python framework used
- Bootstrap - used to create responsive design
- ElephatSQL - used for storing the database
- SQLite - the database used to run the tests 
- Google Fonts - used to get the fonts for the project
- Font Awesome - used to obtain the icons
- Git - used for version control
- GitHub - used to store the code
- GitPod - the development environment
- Heroku - the platform used to deploy the application
- Lucidchart - used to create the database diagram
- Balsamiq Wireframes - used to make the wireframes

# Testing
I used a combination of manual and automated testing to ensure the website functions properly.

## Code Validation
### HTML
- I used [W3C Markup Validation Service](https://validator.w3.org/) to validate the HTML code and it passed with no errors.
- I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the CSS code and it passed with no errors.
- I used [JS Hint](https://jshint.com/) to validate the JavaScript code and it passed with no errors.
- For the Python code I have written code that conforms to the PEP8 style guide. However in the settings.py file, env.py file and in the models.py file, I had to use strings longer than the 79 characters limit.
- I used the Lighthouse development tool to test the website pages for accesibility and the lowest score was 95%.
![Lighthouse Report](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680129131/Dorsia%20PP4%20Images/Readme/lighthouse_test_c0hogv.jpg)

## Manual Testing
I tested this project manually. Especially the JavaScript functionality.
[Here is the link to the MANUAL_TESTING file](/MANUAL_TESTING.md)
## Automated testing
I used the Coverage library to keep track of how much code was covered by the test I've written. After running the coverage report, 98% of the Python code is covered by the tests. The rest of the code was the models. The non-Python code has been tested manually.

## Bugs and fixes
- After finishing the menu page I noticed the Wine cathegory was not displaying the list of items in the backend. The issue appeared to be the code looping through an inexistent meal cathegory. To fix this I put the right parameters to the Django loop.
- **Submit Button Bug** - On the Reservation page, the submit button is 'disabled' by default to prevent the users from submitting a form without a date selected. It is only enabled when the user selects a valid date. I wanted to use the same 'form' but pre-populated on the Edit Reservation page. But when I linked the same script to it, the submit button was 'disabled' by default, and the user had to select the date again, even if they didn't want to change it, only to activate the submit button. To fix it, I added a data attribute to the submit button of both pages so the script can differentiate between them.

# Deployment

# Credits

### settings.py file
- [Code Institute Codestar Sample Project](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/codestar/settings.py) - the MESSAGE_TAGS dictionary
- [Stackoverflow](https://stackoverflow.com/questions/4650509/different-db-for-testing-in-django) - the condition of the if statement

### admin.py file 
- [Code Institute Codestar Sample Project](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/05_building_the_admin_site/blog/admin.py) - the list_filter variable in the BookingAdmin class and the confirm_booking method.

### models.py
- [Code Institute Codestar Sample Project](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/05_building_the_admin_site/blog/models.py) - the confirmed variable in the Booking model.

### test_views.py
- [Stackoverflow](https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login) - the solution on how to create a test user
- [Code Institute Hello Django Sample Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/) - the home page test function

### views.py
- [djangoproject](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator/) - @login_required decorator\
- [Programiz](https://www.programiz.com/python-programming/datetime/strptime) - strptime() method
- [Geeks For Geeks](https://www.geeksforgeeks.org/how-to-convert-datetime-to-date-in-python/) - using of the .date() method to extract the date
- [Stack Overflow](https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django) - the solution to get a user's id
- [Stack Overflow](https://stackoverflow.com/questions/1506901/cleanest-and-most-pythonic-way-to-get-tomorrows-date) - the solution to calculate the date tomorrow
- [Stack Overflow](https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime#:~:text=strptime%20is%20short%20for%20%22parse,seen%20strptime%20used%20since%20DateTime.) - the solution to convert a date to string using .strftime() method

### style.css
- [Font Awesome Advanced](https://fontawesome.com/v5/docs/web/advanced/css-pseudo-elements) - the code used to change the default hamburger icon

### manage_reservations.js
- [Cloudnweb](https://cloudnweb.dev/2020/08/3-efficient-ways-to-get-tomorrow-date-using-javascript/) - the process of getting tomorrow's date

### reservation.js
- [Bootstrap documentation](https://getbootstrap.com/docs/5.0/components/modal/) - the solution to create a modal with a line of JavaScript
- [Scaler](https://www.scaler.com/topics/javascript-disable-button/) - the solution to disabling a button was found on Scaler
- [Free Code Camp](https://www.freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js/#:~:text=To%20handle%20equality%20comparison%2C%20we,getMonth()%20and%20getYear()%20.) - the solution to creating a date out of year, month, day
- [Cloudnweb](https://cloudnweb.dev/2020/08/3-efficient-ways-to-get-tomorrow-date-using-javascript/) - the process of getting tomorrow's date

## Templates
- [w3schools](https://www.w3schools.com/jsref/met_his_go.asp) - the "Go back" button functionality
- [Bootsrap](https://getbootstrap.com/) - Navigation Bar, Striped Tables, Modals, Accordions, Buttons

### base.html
- [Code Institute Codestar Sample Project](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/templates/base.html) - alert messages HTML and Script.


