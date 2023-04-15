const submit = document.querySelector("#submit");

// Fill race description textarea with data from DnD5e api
document.addEventListener("input", function (e) {
  e.preventDefault();
  if (e.target.classList.contains("options")) {
    try {
      let desc = document.querySelector(
        `#${e.target.value.toLowerCase().replace(" ", "-")}`
      ).dataset.desc;
      e.target.nextElementSibling.nextElementSibling.value = desc;
    } catch {}
  }
});

// Collect individual fields to create objects for submission
submit.addEventListener("click", function (e) {
  // e.preventDefault();
  function submit(type) {
    let submitName = document.querySelector(`#${type}-name`).value;
    let submitDesc = document.querySelector(`#${type}-desc`).value;
    let submission = { name: submitName, desc: submitDesc };
    document.querySelector(`#${type}`).value = JSON.stringify(submission);
  }

  submit("race");
  submit("subrace");
  submit("subjob");
  submit("alignment");
});
