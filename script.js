const form = document.querySelector("#request-form");
const result = document.querySelector("#result");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const name = formData.get("name").trim();
  const direction = formData.get("direction");
  const directionLabel = {
    frontend: "Frontend",
    backend: "Backend",
    testing: "Тестирование"
  }[direction];

  result.textContent = `Заявка отправлена, ${name}! Направление: ${directionLabel}.`;
  result.classList.add("visible");
});

form.addEventListener("reset", () => {
  result.textContent = "";
  result.classList.remove("visible");
});
