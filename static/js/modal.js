const elements = document.querySelectorAll(".show-modal, .close-modal");

for (const element of elements) {
    element.addEventListener("click", (event) => {
        const modalId = element.dataset.target;
        const modal = document.getElementById(modalId);
        modal.classList.toggle("active");
    });
}
