const submit = document.querySelector("#submit");

// General document event listener for delete buttons
document.addEventListener("click", function (e) {
  if (e.target.classList.contains("delete")) {
    e.target.parentElement.remove();
  }
});

// Add new condition inputs
document.addEventListener("click", function (e) {
  if (e.target.classList.contains("add")) {
    e.preventDefault();
    let type = e.target.dataset.type;
    let newItem = document.createElement("div");
    document.querySelector(`#${type}-input`).append(newItem);

    let newName = document.createElement("input");
    newName.classList.add(`${type}-name`);
    newName.setAttribute("list", `${type}-datalist`);
    newName.setAttribute("name", `${type}-name`);
    newItem.append("Name");
    newItem.append(newName);

    let newNumber = document.createElement("input");
    newNumber.classList.add(`${type}-number`);
    newNumber.setAttribute("type", "number");
    newItem.append("Name");
    newItem.append(newName);

    let deleteButton = document.createElement("button");
    deleteButton.classList.add("delete");
    deleteButton.innerText = "Delete";
    newProficiency.append(deleteButton);
  }
});

// Collect individual fields to create objects for submission
submit.addEventListener("click", function (e) {
  //   e.preventDefault();
  let submitCurrent = document.querySelector("#weight-current").value;
  let submitMax = document.querySelector("#weight-max").value;
  let submitWeight = { current: submitCurrent, max: submitMax };

  document.querySelector("#weight").value = JSON.stringify(submitWeight);

  function submit(type) {
    let submission = [];
    let names = document.getElementsByClassName(`${type}-name`);
    let numbers = document.getElementsByClassName(`${type}-number`);
    for (let i = 0; i < names.length; i++) {
      submission.push({ name: names[i].value, number: numbers[i].value });
    }
    document.querySelector(`#${type}`).value = JSON.stringify(submission);
  }

  submit("weapons");
  submit("armor");
  submit("tools");
  submit("wallet");
  submit("other");
});
