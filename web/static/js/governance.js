document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn-bar");
    const sections = document.querySelectorAll(".section-content");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            // Remove 'active' class from all buttons
            buttons.forEach((btn) => btn.classList.remove("active"));

            // Add 'active' class to the clicked button
            button.classList.add("active");

            // Hide all sections
            sections.forEach((section) => section.classList.add("d-none"));

            // Show the target section
            const targetSection = document.getElementById(button.dataset.target);
            if (targetSection) {
                targetSection.classList.remove("d-none");
            }
        });
    });
});
