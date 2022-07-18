const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#password');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === 'ReAsEaRcH StUdY') {
        alert('ReAsEaRcH StUdY');
    }

    // testing

    if (nameInput.value === 'testing') {
        alert('nothing for testing right now');
    }
}
