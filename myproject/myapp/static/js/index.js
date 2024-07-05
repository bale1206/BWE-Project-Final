document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed.');

    // Select elements
    const form = document.getElementById('form');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const password2 = document.getElementById('password2');

    console.log('Form element:', form);

    // Check if the form exists
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            if (validateInputs()) {
                form.submit();
            }
        });
    } else {
        console.error('Form element not found.');
    }

    // Function to set error message
    const setError = (element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = message;
        inputControl.classList.add('error');
        inputControl.classList.remove('success');
    };

    // Function to set success message
    const setSuccess = (element) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = '';
        inputControl.classList.add('success');
        inputControl.classList.remove('error');
    };

    // Function to validate email
    const isValidEmail = (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    };
    

    // Function to validate inputs
    const validateInputs = () => {
        const emailValue = email.value.trim();
        const passwordValue = password.value.trim();
        const password2Value = password2.value.trim();

        if (emailValue === '') {
            setError(email, 'Ingrese el correo electrónico');
        } else if (!isValidEmail(emailValue)) {
            setError(email, 'Ingrese un correo electrónico válido');
        } else {
            setSuccess(email);
        }

        if (passwordValue === '') {
            setError(password, 'Ingrese la contraseña');
        } else if (passwordValue.length < 8) {
            setError(password, 'La contraseña debe contener al menos 8 caracteres.');
        } else {
            setSuccess(password);
        }

        if (password2Value === '') {
            setError(password2, 'Por favor confirmar contraseña');
        } else if (password2Value !== passwordValue) {
            setError(password2, 'Las contraseñas no coinciden');
        } else {
            setSuccess(password2);
        }
    };
});
