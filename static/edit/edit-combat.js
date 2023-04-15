const attackAdd = document.querySelector("#attack-add");
const attackInput = document.querySelector("#attack-input");
const submit = document.querySelector("#submit");

// General document event listener for buttons
document.addEventListener("click", function (e) {
  // Delete attack inputs
  if (e.target.classList.contains("delete")) {
    e.target.parentElement.remove();
  }
});

// Add new attack inputs
attackAdd.addEventListener("click", function (e) {
  e.preventDefault();

  let newAttack = document.createElement("div");
  attackInput.append(newAttack);

  let newName = document.createElement("input");
  newName.classList.add("attack-name");
  newName.type = "text";
  newAttack.append("Name");
  newAttack.append(newName);

  let newThrows = document.createElement("input");
  newThrows.classList.add("attack-throws");
  newThrows.type = "number";
  newAttack.append("Throws");
  newAttack.append(newThrows);

  let newDie = document.createElement("input");
  newDie.classList.add("attack-die");
  newDie.type = "number";
  newAttack.append("Die");
  newAttack.append(newDie);

  let newNumber = document.createElement("input");
  newNumber.classList.add("attack-number");
  newNumber.type = "number";
  newAttack.append("Number");
  newAttack.append(newNumber);

  let deleteButton = document.createElement("button");
  deleteButton.classList.add("delete");
  deleteButton.innerText = "Delete";
  newAttack.append(deleteButton);
});

// Collect fields to create object for submission
submit.addEventListener("click", function () {
  // Collect HP "current" and "max"
  let submitCurrent = document.querySelector("#ki-current").value;
  let submitMax = document.querySelector("#ki-max").value;
  let submitKi = { current: submitCurrent, max: submitMax };

  document.querySelector("#ki").value = JSON.stringify(submitKi);

  // Collect attack "name", "throws", "die", and "number"
  let attackList = [];
  let attackName = document.getElementsByClassName("attack-name");
  let attackThrows = document.getElementsByClassName("attack-throws");
  let attackDie = document.getElementsByClassName("attack-die");
  let attackNumber = document.getElementsByClassName("attack-number");

  for (let i = 0; i < attackName.length; i++) {
    attackList.push({
      name: attackName[i].value,
      throws: attackThrows[i].value,
      die: attackDie[i].value,
      number: attackNumber[i].value,
    });
  }
  document.querySelector("#attacks").value = JSON.stringify(attackList);
});
