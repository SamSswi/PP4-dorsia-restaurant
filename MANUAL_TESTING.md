# Manual Testing

[Back to the main README file](/README.md)

## Epic 1 - Core website functionality

### User Stories

5. As a User I can easily and intuitively navigate the website so that I can view the content I am interested in

9. As a User I can access a front-end interface that meets accessibility guidelines and follows the principles of UX design so that I can interact with the web application in an intuitive and easy-to-use way

10. As a User I can see the key information on the home page so that I won't have to search for it

The homepage provides the user with key information. A brief information about the restaurant, the opening hours, the address and the contact information. 

The navigation bar and the button bar provide the user with the oportunity to access all the website pages and authenticate themselves.

## Epic 2 - Admin functionality

### User Stories

1. As an Admin I can log in as a super user so that I can access the backend of the website

2. As an Admin I can make changes to the menu items so that the users sees an up-to-date menu

By adding the '/admin' extension to the website link, the admin can access the backend with the superuser credentials. 

In the backend, the admin can create, edit and delete the menu items primarily but also the admin can edit and delete user information and reservations.

## Epic 3 - User Authentication

### User Stories

6. As a user I can Log In or Sign Up with email and password so that I can create an account and enjoy the services of the restaurant

The navbar displays different links depending on the status of the user. If the user is not logged in, they are presented with the options to Log In or Register.

On the Log In page, the users are given the opportunity to register if they're not registered yet. Only logged-in users can make reservations. Whenever the registers, logs in or logs out, they're shown a success message to confirm their action succeeded.

## Epic 4 - Display the menu

### User Stories
3. As a User I can view detailed info about the items in the menu so that I have a better familiarity with the particularities of each meal served

4. As a User I can view the items in the restaurant menu in a clear way so that I know beforehand what dishes and drinks are served, and can get familiar with the menu of the restaurant

The menu for Food and Drinks can be viewed by accessing the Menu page. Each menu item has a description where more details about it are displayed.

## Epic 5 - Reservation Functionality

### User Stories
7. As a User I can make a reservation at the restaurant so that I can enjoy the foods, drinks, and services of this restaurant

8. As a User I can View and Edit my bookings so that I can personally manage my reservations without contacting the restaurant

From the Reservation page the user can fill a form with the desired information about a booking to make a reservation.

Users that are not logged-in, cannot access the Reservation page but are redirected to the Log In page instead.

A logged-in user can access the Manage Reservations page and edit or delete a reservation. Whenever the user executes one of these functionalities, they're shown a success message to confirm their action succeeded.
<br>
<hr>

# JavaScript Testing
I have written a few JavaScript functions to handle changes when the user selects a booking date and to remove the edit and delete functionality from the Manage Reservations pages for the reservations that have expired or are happening too soon to be relevant to edit them. This prevents the user from editing an expired reservation or a reservation happening too soon to be modified.
![Screenshot of the manage reservations page past](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680049446/Dorsia%20PP4%20Images/Readme/manage_reservations_page_past_oua9j0.jpg)

Another instance where I used JavaScript was to trigger a modal when an user enters a date from the past or too early in the future to be relevant.

![Screenshot of the modal](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680051014/Dorsia%20PP4%20Images/Readme/wrong_date_modal_tnt8vf.jpg)

The last task performed by the script is disabling the 'Submit' button whenever the user enters a wrong date, and keeping the button 'disabled' until the user enters a valid date. This prevents the user from submitting an invalid form.

![Screenshot of the submit button wrong time](https://res.cloudinary.com/dclq2ghzy/image/upload/v1680051136/Dorsia%20PP4%20Images/Readme/submit_button_bad_date_gc6muq.jpg)

[Back to the main README file](/README.md)





