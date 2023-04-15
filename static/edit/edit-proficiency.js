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
    let newProficiency = document.createElement("div");
    document.querySelector(`#${type}-input`).append(newProficiency);

    let newName = document.createElement("input");
    newName.classList.add(`${type}-name`);
    newName.setAttribute("list", `${type}-datalist`);
    newName.setAttribute("name", `${type}-name`);
    newProficiency.append("Name");
    newProficiency.append(newName);

    let deleteButton = document.createElement("button");
    deleteButton.classList.add("delete");
    deleteButton.innerText = "Delete";
    newProficiency.append(deleteButton);
  }
});

// Collect individual fields to create objects for submission
submit.addEventListener("click", function (e) {
  //   e.preventDefault();
  function submit(type) {
    let submission = [];
    let names = document.getElementsByClassName(`${type}-name`);
    for (let name of names) {
      submission.push({ name: name.value });
    }
    document.querySelector(`#${type}`).value = JSON.stringify(submission);
  }

  submit("skills");
  submit("weapons");
  submit("armor");
  submit("tools");
  submit("languages");
  submit("traits");
  submit("features");
});
