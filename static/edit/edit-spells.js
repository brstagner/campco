const knownAdd = document.querySelector("#known-add");
const knownInput = document.querySelector("#known-input");
const submit = document.querySelector("#submit");

// General document event listener for delete buttons
document.addEventListener("click", function (e) {
  if (e.target.classList.contains("delete")) {
    e.target.parentElement.remove();
  }
});

// Add new known spell inputs
knownAdd.addEventListener("click", function (e) {
  e.preventDefault();

  let newSpell = document.createElement("div");
  knownInput.append(newSpell);

  let newName = document.createElement("input");
  newName.classList.add("known-name");
  newName.setAttribute("list", "spells-datalist");
  newName.type = "text";
  newSpell.append("Name");
  newSpell.append(newName);

  let newLevel = document.createElement("input");
  newLevel.classList.add("known-level");
  newLevel.type = "number";
  newSpell.append("level");
  newSpell.append(newLevel);

  let newDesc = document.createElement("textarea");
  newDesc.classList.add("known-desc");
  newSpell.append("desc");
  newSpell.append(newDesc);

  let deleteButton = document.createElement("button");
  deleteButton.classList.add("delete");
  deleteButton.innerText = "Delete";
  newSpell.append(deleteButton);
});

// Event listener for adding new spell inputs at each level
for (let n = 0; n < 10; n++) {
  document.querySelector(`#lv${n}-add`).addEventListener("click", function (e) {
    e.preventDefault();

    let newSpell = document.createElement("div");
    document.querySelector(`#lv${n}-input`).append(newSpell);

    let newName = document.createElement("input");
    newName.classList.add(`lv${n}-name`);
    newName.setAttribute("list", "spells-datalist");
    newName.type = "text";
    newSpell.append("Name");
    newSpell.append(newName);

    let newNumber = document.createElement("input");
    newNumber.classList.add(`lv${n}-number`);
    newNumber.type = "number";
    newSpell.append("number");
    newSpell.append(newNumber);

    let deleteButton = document.createElement("button");
    deleteButton.classList.add("delete");
    deleteButton.innerText = "Delete";
    newSpell.append(deleteButton);
  });
}

// Collect fields to create object for submission
submit.addEventListener("click", function (e) {
  // Collect known spells
  let knownList = [];
  let knownName = document.getElementsByClassName("known-name");
  let knownLevel = document.getElementsByClassName("known-level");
  let knownDesc = document.getElementsByClassName("known-desc");

  for (let i = 0; i < knownName.length; i++) {
    knownList.push({
      name: knownName[i].value,
      level: knownLevel[i].value,
      desc: knownDesc[i].value,
    });
  }
  document.querySelector("#known").value = JSON.stringify(knownList);

  // Collect spells at each level
  for (let n = 0; n < 10; n++) {
    let spellList = [];
    let spellName = document.getElementsByClassName(`lv${n}-name`);
    let spellNumber = document.getElementsByClassName(`lv${n}-number`);
    for (let i = 0; i < spellName.length; i++) {
      spellList.push({
        name: spellName[i].value,
        number: spellNumber[i].value ? spellNumber[i].value : 0,
      });
    }
    document.querySelector(`#lv${n}`).value = JSON.stringify(spellList);
  }
});

// Fill spell description textarea with data from DnD5e api
document.addEventListener("input", function (e) {
  e.preventDefault();
  if (e.target.classList.contains("known-name")) {
    try {
      let desc = document.querySelector(
        `#${e.target.value.toLowerCase().replaceAll(" ", "-")}`
      ).dataset.desc;
      e.target.nextElementSibling.nextElementSibling.value = desc;
    } catch {}
  }
});
