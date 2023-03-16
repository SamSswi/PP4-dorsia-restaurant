// https://github.com/SamSswi/Rock-Paper-Scissors-Lizard-Spock/blob/main/assets/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    const dateInput = document.getElementById('booking-date')
    const submitBtn = document.getElementById('submit-btn')
    // https://getbootstrap.com/docs/5.0/components/modal/
    const myModal = new bootstrap.Modal(document.getElementById('exampleModalCenter'))
    const closeModalButtons = document.querySelectorAll('[data-dismiss="modal"]')
    // https://www.scaler.com/topics/javascript-disable-button/
    submitBtn.disabled = true
    dateInput.addEventListener('change', () => {
        const inputYear = Number(dateInput.value.split('-')[0])
        const inputMonth = Number(dateInput.value.split('-')[1]) - 1
        const inputDay = Number(dateInput.value.split('-')[2])

        // https://cloudnweb.dev/2020/08/3-efficient-ways-to-get-tomorrow-date-using-javascript/
        const today = new Date()
        const tomorrow = new Date()
        tomorrow.setDate(today.getDate() + 1)

        // // https://www.w3schools.com/jsref/jsref_obj_date.asp the get methods are from this link
        const dayTomorrow = tomorrow.getDate()
        const monthTomorrow = tomorrow.getMonth()
        const yearTomorrow = tomorrow.getFullYear()

        // https://www.freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js/#:~:text=To%20handle%20equality%20comparison%2C%20we,getMonth()%20and%20getYear()%20.
        const createDate = (year, month, day) => new Date(year, month - 1, day).getTime()

        const selectedDate = createDate(inputYear, inputMonth, inputDay)
        const tomorrowDate = createDate(yearTomorrow, monthTomorrow, dayTomorrow)

        if (selectedDate < tomorrowDate) {
            submitBtn.disabled = true
            myModal.show()
        } else {
            submitBtn.disabled = false
        }

        for (let i = 0; i < closeModalButtons.length; i++) {
            closeModalButtons[i].addEventListener('click', function () {
                myModal.hide()
            })
        }

    })
})