const addSnapButton = document.querySelector("#add-snap");
const totalForms = document.querySelector("#id_snaps-TOTAL_FORMS");
const appendTarget = document.querySelector("#snap-form-list");

const addForm = (event) => {
    event.preventDefault();

    const snapForms = document.querySelectorAll(".snap-form");
    let formNum = snapForms.length;

    const newSnapForm = snapForms[snapForms.length - 1].cloneNode(true);
    const formRegex = new RegExp(`snaps-(\\d){1}-`, "g");

    newSnapForm.innerHTML = newSnapForm.innerHTML.replace(
        formRegex,
        `snaps-${formNum}-`
    );

    appendTarget.append(newSnapForm);

    totalForms.setAttribute("value", `${formNum + 1}`);
};

addSnapButton.addEventListener("click", addForm);
