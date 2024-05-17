function validateForm() {
    var occupation = document.getElementById('Occupation').value;
    if (occupation !== '' && occupation[0] !== occupation[0].toUpperCase()) {
        alert('The first letter of the Occupation must be a capital letter!');
        return false;
    }
    var inputs = document.getElementsByTagName('input');
    var selects = document.getElementsByTagName('select');
    var isValid = true;
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === '') {
            inputs[i].style.borderColor = 'red'; // Highlighting the border colour
            isValid = false;
        } else {
            inputs[i].style.borderColor = '';  // Resetting border colour
        }
    }
    for (var i = 0; i < selects.length; i++) {
        if (selects[i].value === '') {
            selects[i].style.borderColor = 'red'; // Highlighting the border colour
            isValid = false;
        } else {
            selects[i].style.borderColor = '';  // Resetting border colour
        }
    }
    if (!isValid) {
        alert('Please fill in all the fields or Make sure that you selected an option for all fields with a selection option!');
    }
    return isValid;
}
window.onload = function() {
    // Selecting all input fields except the one for Occupation
    var inputs = document.querySelectorAll('input:not(#Occupation)');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('input', function(e) {
            e.target.value = e.target.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');
        });
    }

    // Selecting the input field for Occupation
    var occupationInput = document.querySelector('#Occupation');
    occupationInput.addEventListener('input', function(e) {
        e.target.value = e.target.value.replace(/[^a-zA-Z ]/g, '');
    });
}