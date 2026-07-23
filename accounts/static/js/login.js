const loginForm = document.getElementById("loginForm");

const username = document.getElementById("username");
const password = document.getElementById("password");

const usernameError = document.getElementById("usernameError");
const passwordError = document.getElementById("passwordError");

const togglePassword = document.getElementById("togglePassword");

const loginButton = document.getElementById("loginButton");


/* =========================
   SHOW / HIDE PASSWORD
========================= */

togglePassword.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";

        togglePassword.textContent = "Hide";

    } else {

        password.type = "password";

        togglePassword.textContent = "Show";

    }

});


/* =========================
   FORM VALIDATION
========================= */

loginForm.addEventListener("submit", function (event) {

    let isValid = true;


    usernameError.textContent = "";
    passwordError.textContent = "";


    if (username.value.trim() === "") {

        usernameError.textContent =
            "Please enter your username.";

        isValid = false;

    }


    if (password.value.trim() === "") {

        passwordError.textContent =
            "Please enter your password.";

        isValid = false;

    }


    if (!isValid) {

        event.preventDefault();

        return;

    }


    loginButton.classList.add("loading");

    loginButton.disabled = true;

});