// Collect individual fields to create objects for submission
const submit = document.querySelector("#submit");

submit.addEventListener("click", function (e) {
  e.preventDefault();
  let campaignName = document.querySelector("#campaign-name").value;
  let campaignId = document.querySelector("#campaign-id").value;
  campaignId.value = campaignName[-1];
});
