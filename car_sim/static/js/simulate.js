// ========================
// Simulation Frontend Logic
// ========================

function calculateScore(wing, ride) {
    // simple "fake" scoring for UI feedback
    let score = 100;

    score -= wing * 1.2;
    score -= ride * 0.2;

    return Math.max(score, 0);
}

function updatePreview() {
    const wing = document.querySelector("input[name='wing_angle']");
    const ride = document.querySelector("input[name='ride_height']");
    const output = document.getElementById("liveScore");

    if (!wing || !ride || !output) return;

    const score = calculateScore(Number(wing.value), Number(ride.value));
    output.textContent = "Estimated Aero Score: " + score.toFixed(1);
}

function validateInputs(wing, ride) {
    if (wing < 0 || wing > 30) {
        return "Wing angle must be between 0–30°";
    }
    if (ride < 0 || ride > 200) {
        return "Ride height must be between 0–200 mm";
    }
    return null;
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#configForm");

    if (!form) return;

    const inputs = form.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("input", updatePreview);
    });

    form.addEventListener("submit", (e) => {
        const wing = Number(document.querySelector("input[name='wing_angle']").value);
        const ride = Number(document.querySelector("input[name='ride_height']").value);

        const error = validateInputs(wing, ride);

        if (error) {
            alert(error);
            e.preventDefault();
        }
    });
});
