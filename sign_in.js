document.addEventListener("DOMContentLoaded", function () {
  const passwordInput = document.getElementById("password");
  const togglePasswordBtn = document.getElementById("toggle-password");
  const passwordError = document.getElementById("password-error");
  const submitBtn = document.getElementById("submit-btn");

  // Function to toggle password visibility
  togglePasswordBtn.addEventListener("click", function () {
    const type =
      passwordInput.getAttribute("type") === "password" ? "text" : "password";
    passwordInput.setAttribute("type", type);
    togglePasswordBtn.textContent = type === "password" ? "Show" : "Hide";
  });

  // Function to validate password length
  passwordInput.addEventListener("input", function () {
    const password = passwordInput.value;
    if (password.length > 20) {
      passwordError.textContent = "Password is too long (max 20 characters)";
      submitBtn.disabled = true;
    } else {
      passwordError.textContent = "";
      submitBtn.disabled = false;
    }
  });
});
