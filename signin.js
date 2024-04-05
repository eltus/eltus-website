// Get references to elements
const passwordInput = document.getElementById("password");
const showPasswordButton = document.getElementById("show-password");
const signInForm = document.getElementById("signin-form");
const googleSignInButton = document.getElementById("google-signin-btn");

// Add event listener to show password
showPasswordButton.addEventListener("click", function () {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPasswordButton.textContent = "Hide";
  } else {
    passwordInput.type = "password";
    showPasswordButton.textContent = "Show";
  }
});

// Add event listener to sign in form
signInForm.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission

  const email = signInForm.email.value;
  const password = signInForm.password.value;

  // Sign in with email and password using Firebase Authentication
  firebase
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed in successfully
      const user = userCredential.user;
      console.log("Signed in as:", user.uid);
      // Redirect to dashboard or desired page
    })
    .catch((error) => {
      // Sign in failed, handle error
      console.error("Sign in error:", error);
      // Display error message to the user
    });
});

// Add event listener to Google sign-in button
googleSignInButton.addEventListener("click", function () {
  const provider = new firebase.auth.GoogleAuthProvider();
  firebase
    .auth()
    .signInWithPopup(provider)
    .then((result) => {
      // Google sign-in successful
      const user = result.user;
      console.log("Signed in with Google as:", user.uid);
      // Redirect to dashboard or desired page
    })
    .catch((error) => {
      // Google sign-in failed, handle error
      console.error("Google sign-in error:", error);
      // Display error message to the user
    });
});
