document.addEventListener("DOMContentLoaded", function () {
    // Calling the elements needed from the html file
    const dateInput = document.getElementById('booking-date')
    const submitBtn = document.getElementById('submit-btn')
    // The solution to create a modal with a line of JavaScript was taken from Bootstrap documentation
    // https://getbootstrap.com/docs/5.0/components/modal/
    const myModal = new bootstrap.Modal(document.getElementById('exampleModalCenter'))
    const closeModalButtons = document.querySelectorAll('[data-dismiss="modal"]')

    // Determining the initial status of the submit button
    const startDisabled = submitBtn.dataset.disabled === 'true'
    // The solution to disabling a button was found on Scaler
    // https://www.scaler.com/topics/javascript-disable-button/
    submitBtn.disabled = startDisabled

    // The solution to creating a date out of year, month, day
    // was found on Free Code Camp
    // https://www.freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js/#:~:text=To%20handle%20equality%20comparison%2C%20we,getMonth()%20and%20getYear()%20.
    const createDate = (year, month, day) => new Date(year, month - 1, day).getTime()

    // Creating a date for tomorrow
    function setTomorrowDate() {
        // The process of getting tomorrow's date was inspired from Cloudnweb
        // https://cloudnweb.dev/2020/08/3-efficient-ways-to-get-tomorrow-date-using-javascript/
        const today = new Date()
        const tomorrow = new Date()
        tomorrow.setDate(today.getDate() + 1)
        // The .get... methods are taken from W3Schools
        // https://www.w3schools.com/jsref/jsref_obj_date.asp
        const dayTomorrow = tomorrow.getDate()
        const monthTomorrow = tomorrow.getMonth()
        const yearTomorrow = tomorrow.getFullYear()
        const tomorrowDate = createDate(yearTomorrow, monthTomorrow, dayTomorrow)
        return tomorrowDate
    }

    // Add an event listener to catch any changes the user makes to the date input element
    dateInput.addEventListener('change', () => {

        // Converting the input strings to numbers
        const inputYear = Number(dateInput.value.split('-')[0])
        const inputMonth = Number(dateInput.value.split('-')[1]) - 1
        const inputDay = Number(dateInput.value.split('-')[2])
        
        // creating constants for tomorrow date and the input date
        const selectedDate = createDate(inputYear, inputMonth, inputDay)
        const tomorrowDate = setTomorrowDate()

        // comparing the input date with the tomorrow date to determine the status of the submit button and the modal
        if (selectedDate < tomorrowDate) {
            submitBtn.disabled = true
            myModal.show()
        } else {
            submitBtn.disabled = false
        }
        
        // adding functionality to the modal close buttons
        for (let i = 0; i < closeModalButtons.length; i++) {
            closeModalButtons[i].addEventListener('click', function () {
                myModal.hide()
            })
        }

    })
})