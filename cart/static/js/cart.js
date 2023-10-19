// Increment and Decrement CART Quantity from Cart.html page

import { updateCartQuantityAPI } from "../../../static/js/apiUpdateCartQty.js";

// Get all the increment and decrement buttons
const incrementButtons = document.querySelectorAll(".increment");
const decrementButtons = document.querySelectorAll(".decrement");
const grand_total_element = document.getElementById("grand_total_price");

// Add event listeners to each button
incrementButtons.forEach(function (button) {
  button.addEventListener("click", async function () {
    // Find the corresponding quantity input
    const quantityInput = button.parentElement.querySelector(".quantity");

    // Increment the value
    const total_Quantity = parseInt(quantityInput.value) + 1;
    quantityInput.value = total_Quantity;

    const product_Id = quantityInput.getAttribute("data-product-id");
    const data = await updateCartQuantityAPI(product_Id, total_Quantity);

    const cart_container = button.closest(".cart_container");
    const sub_total_element = cart_container.querySelector(".cart_total_price");
    sub_total_element.textContent = data.sub_total;

    grand_total_element.textContent = data.grand_total;
  });
});

decrementButtons.forEach(function (button) {
  button.addEventListener("click", async function () {
    // Find the corresponding quantity input
    const quantityInput = button.parentElement.querySelector(".quantity");

    const total_Quantity = parseInt(quantityInput.value) - 1;
    // Double Ensuring Qty doesnt go below or equals to 0
    if (total_Quantity <= 0) {
      // Changing the COLOR of info-message here.
      const infoMessage =
        button.parentElement.parentElement.parentElement.parentElement.querySelector(
          ".info-message"
        );
      infoMessage.style.display = "block";
      infoMessage.textContent =
        "Quantity cant be '0', delete the cart Instead! ";

      setTimeout(() => {
        infoMessage.style.display = "none";
      }, 2000);
    } else {
      quantityInput.value = total_Quantity;
      const product_Id = quantityInput.getAttribute("data-product-id");
      const data = await updateCartQuantityAPI(product_Id, total_Quantity);

      const cart_container = button.closest(".cart_container");
      const sub_total_element =
        cart_container.querySelector(".cart_total_price");
      sub_total_element.textContent = data.sub_total;

      grand_total_element.textContent = data.grand_total;
    }
  });
});
