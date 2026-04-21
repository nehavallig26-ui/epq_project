// ========================
// Auth Validation + UX
// ========================

function showMessage(message, type="error") {
    const box = document.getElementById("formMessage");
    if (!box) return;

    box.textContent = message;
    box.className = type;
}

function validateCredentials(username, password) {
    if (username.length < 3) {
        return "Username must be at least 3 characters";
    }
    if (password.length < 5) {
        return "Password must be at least 5 characters";
    }
    return null;
}

document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            const username = form.querySelector("input[name='username']");
            const password = form.querySelector("input[name='password']");

            if (username && password) {
                const error = validateCredentials(username.value, password.value);

                if (error) {
                    e.preventDefault();
                    showMessage(error, "error");
                }
            }
        });
    });
});
