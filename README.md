# Dorsia Restaurant
![Screenshot of a am I responsive](https://myoctocat.com/assets/images/base-octocat.svg)

[Live application can be found here](https://pages.github.com/)

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

9. As a User I can ** a front-end interface that meets accessibility guidelines and follows the principles of UX design** so that I can interact with the web application in an intuitive and easy-to-use way

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

![Screenshot of a am I responsive](https://myoctocat.com/assets/images/base-octocat.svg)

## Wireframes
[The Wireframes can be viewed here.](https://en.wikipedia.org/wiki/American_Psycho)

Note: The actual website can differ from the original wireframes.

## Colors
The colors I chose for this website are a shade of bone (##E3DAC9) and a warm gray (#6E7178) with subtle variations. It is not designed to be an attention-grabbing color combination, but it is supposed to suggest warmth and elegance. 

# Features

## Navigation bar
The navigation bar contains links to all the relevant active pages. The Edit Reservation and Delete Reservation pages can be accessed from the Manage Reservations page, as they require a booking_id to know what reservation to act upon.

If the user is logged in, the right side of the Navigation Bar displays the following links: "Manage Reservations" and "Log Out".
![Screenshot of the navigation bar initial](https://myoctocat.com/assets/images/base-octocat.svg)
If the user is not logged in, then the options on the right side of the Navigation bar are to log in or register.
![Screenshot of the navigation bar logged-in user](https://myoctocat.com/assets/images/base-octocat.svg)
The navigation bar is responsive and collapses on smaller screens.
![Screenshot of the navigation bar collapsed](https://myoctocat.com/assets/images/base-octocat.svg)


## Home page
The home page features a landing area (where the name "Dorsia" is displayed), a bar with buttons allowing the user to access the menu or make a reservation, and an About Us section with a brief description of the restaurant.
![Screenshot of the home page](https://myoctocat.com/assets/images/base-octocat.svg)

## Menu
The menu page displays separately the sections of the menu. Each item has a name and a description. The menu items can be added, edited or deleted by the admin in the backend.
![Screenshot of the menu page](https://myoctocat.com/assets/images/base-octocat.svg)

## Make a Reservation
This page can be accessed only by the logged-in users. The visitors who are not registered yet, are redirected to the Sign Up page.
The page conatins a form the user can fill. The fields are not pre-populated.


