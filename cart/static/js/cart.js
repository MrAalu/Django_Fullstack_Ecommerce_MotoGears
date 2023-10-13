document.getElementById("increment").addEventListener("click", function () {
  const quantityInput = document.getElementById("quantity");
  quantityInput.value = parseInt(quantityInput.value, 10) + 1;
});

document.getElementById("decrement").addEventListener("click", function () {
  const quantityInput = document.getElementById("quantity");
  if (parseInt(quantityInput.value, 10) > 1) {
    quantityInput.value = parseInt(quantityInput.value, 10) - 1;
  }
});
