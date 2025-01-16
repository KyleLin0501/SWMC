document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn-bar");

    buttons.forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();

            // Remove 'active' class from all buttons
            buttons.forEach((btn) => btn.classList.remove("active"));

            // Add 'active' class to the clicked button
            button.classList.add("active");

            // Scroll to the target section
            const targetId = button.getAttribute("data-target");
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
            }
        });
    });
});