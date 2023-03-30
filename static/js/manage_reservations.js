document.addEventListener("DOMContentLoaded", function () {
    const reservationItems = document.getElementsByClassName('accordion-item')
    // Creating a date for tomorrow
    function setTomorrowDate() {
        // The process of getting tomorrow's date was inspired from Cloudnweb
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