// Increment and Decrement CART Quantity from Cart.html page

// Get all the increment and decrement buttons
const incrementButtons = document.querySelectorAll(".increment");
const decrementButtons = document.querySelectorAll(".decrement");

// Add event listeners to each button
incrementButtons.forEach(function (button, index) {
  button.addEventListener("click", function () {
    // Find the corresponding quantity input
    const quantityInput = button.parentElement.querySelector(".quantity");

    // Increment the value
    quantityInput.value = parseInt(quantityInput.value) + 1;
  });
});

decrementButtons.forEach(function (button, index) {
  button.addEventListener("click", function () {
    // Find the corresponding quantity input
    const quantityInput = button.parentElement.querySelector(".quantity");

    // Ensure the value doesn't go below the minimum
    const newValue = Math.max(
      parseInt(quantityInput.value) - 1,
      parseInt(quantityInput.getAttribute("min"))
    );
    quantityInput.value = newValue;
  });
});
