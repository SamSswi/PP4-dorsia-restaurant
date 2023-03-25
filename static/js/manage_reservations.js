// https://github.com/SamSswi/Rock-Paper-Scissors-Lizard-Spock/blob/main/assets/js/script.js

document.addEventListener("DOMContentLoaded", function () {
    const reservationItems = document.getElementsByClassName('accordion-item')
    // https://www.freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js/#:~:text=To%20handle%20equality%20comparison%2C%20we,getMonth()%20and%20getYear()%20.

    // Creating a date for tomorrow
    function setTomorrowDate() {
        // https://cloudnweb.dev/2020/08/3-efficient-ways-to-get-tomorrow-date-using-javascript/
        const today = new Date()
        const tomorrow = new Date()
        tomorrow.setDate(today.getDate() + 1)
        return tomorrow
    }
    
    // Compare the reservation date to the tomorrow date
    for (const item of reservationItems) {
        const reservationDate = new Date(item.dataset.bookingdate)
        const dateTomorrow = setTomorrowDate()
        if (reservationDate.getTime() < dateTomorrow) {
            item.querySelector('.action-btns').style.display = 'none'
        }
    }
})