const hdAdd = document.querySelector("#hd-add");
const hdInput = document.querySelector("#hd-input");
const conditionsAdd = document.querySelector("#conditions-add");
const conditionsInput = document.querySelector("#conditions-input");
const submit = document.querySelector("#submit");

// General document event listener for buttons
document.addEventListener("click", function (e) {
  // Clear condition description textarea
  if (e.target.classList.contains("clear")) {
    e.target.parentElement.nextElementSibling.value = null;
  }
  // Delete HD or conditions inputs
  if (e.target.classList.contains("delete")) {
    e.target.parentElement.remove();
  }
});

// Fill condition description textarea with data from DnD5e api
document.addEventListener("input", function (e) {
  e.preventDefault();
  if (e.target.classList.contains("condition-name")) {
    try {
      let desc = document.querySelector(`#${e.target.value}`).dataset.desc;
      e.target.nextElementSibling.nextElementSibling.value = desc;
    } catch {}
  }
});

// Add new HD inputs
hdAdd.addEventListener("click", function (e) {
  e.preventDefault();

  let newHD = document.createElement("div");
  hdInput.append(newHD);

  let newNumber = document.createElement("input");
  newNumber.classList.add("hd-number");
  newNumber.type = "number";
  newHD.append("Number");
  newHD.append(newNumber);

  let newDie = document.createElement("input");
  newDie.classList.add("hd-die");
  newDie.type = "number";
  newHD.append("Die Type");
  newHD.append(newDie);

  let newModifier = document.createElement("input");
  newModifier.classList.add("hd-modifier");
  newModifier.type = "number";
  newHD.append("Modifier");
  newHD.append(newModifier);

  let deleteButton = document.createElement("button");
  deleteButton.classList.add("delete");
  deleteButton.innerText = "Delete";
  newHD.append(deleteButton);
});

// Add new condition inputs
conditionsAdd.addEventListener("click", function (e) {
  e.preventDefault();

  let newCondition = document.createElement("div");
  conditionsInput.append(newCondition);

  let newName = document.createElement("input");
  newName.classList.add("condition-name");
  newName.setAttribute("list", "condition-name-datalist");
  newName.setAttribute("name", "condition-name");
  newCondition.append("Name");
  newCondition.append(newName);

  let descDiv = document.createElement("div");
  descDiv.classList.add("row");
  descDiv.append("Description");
  newCondition.append(descDiv);

  let clear = document.createElement("button");
  clear.classList.add("clear");
  clear.append("clear");

  descDiv.append(clear);
  let newDesc = document.createElement("textarea");
  newDesc.classList.add("condition-desc");
  descDiv.append(newDesc);
  newCondition.append(newDesc);

  let deleteButton = document.createElement("button");
  deleteButton.classList.add("delete");
  deleteButton.innerText = "Delete";
  newCondition.append(deleteButton);
});

// Collect individual fields to create objects for submission
submit.addEventListener("click", function () {
  // Collect HP "current" and "max"
  let submitCurrent = document.querySelector("#hp-current").value;
  let submitMax = document.querySelector("#hp-max").value;
  let submitHP = { current: submitCurrent, max: submitMax };

  document.querySelector("#hp").value = JSON.stringify(submitHP);

  // Collect HD "number", "die", and "modifier"
  let hdList = [];
  let hdNumber = document.getElementsByClassName("hd-number");
  let hdDie = document.getElementsByClassName("hd-die");
  let hdModifier = document.getElementsByClassName("hd-modifier");
  for (let i = 0; i < hdNumber.length; i++) {
    hdList.push({
      number: hdNumber[i].value,
      die: hdDie[i].value,
      modifier: hdModifier[i].value,
    });
  }
  document.querySelector("#hd").value = JSON.stringify(hdList);

  // Collect conditions "name" and "desc"
  let conditionsList = [];
  let conditionName = document.getElementsByClassName("condition-name");
  let conditionDesc = document.getElementsByClassName("condition-desc");
  for (let i = 0; i < conditionName.length; i++) {
    conditionsList.push({
      name: conditionName[i].value,
      desc: conditionDesc[i].value,
    });
  }
  document.querySelector("#conditions").value = JSON.stringify(conditionsList);
});
