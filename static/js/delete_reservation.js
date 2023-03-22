document.addEventListener("DOMContentLoaded", function () {
    const myModal = new bootstrap.Modal(document.getElementById('exampleModalCenter'))
    const closeModalButtons = document.querySelectorAll('[data-dismiss="modal"]')
    for (let i = 0; i < closeModalButtons.length; i++) {
        closeModalButtons[i].addEventListener('click', function () {
            myModal.hide()
        })
    }
})