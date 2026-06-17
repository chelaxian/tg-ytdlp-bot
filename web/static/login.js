(function() {
    const form = document.getElementById("login-form");
    if (!form) return;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const btn = document.getElementById("login-btn");
        const errorMsg = document.getElementById("error-msg");
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        btn.disabled = true;
        btn.textContent = "Logging in...";
        errorMsg.classList.remove("show");

        try {
            const response = await fetch("/api/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            if (response.ok) {
                window.location.href = "/";
            } else {
                const data = await response.json();
                let errorText = data.detail || "Login failed";
                if (errorText.includes("Too many failed attempts")) {
                    errorText += "...";
                }
                errorMsg.textContent = errorText;
                errorMsg.classList.add("show");
            }
        } catch (err) {
            errorMsg.textContent = "Network error. Please try again.";
            errorMsg.classList.add("show");
        } finally {
            btn.disabled = false;
            btn.textContent = "Login";
        }
    });
})();