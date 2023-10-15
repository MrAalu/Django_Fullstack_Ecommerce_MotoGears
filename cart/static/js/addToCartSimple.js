// This JS is LINKED to layout/Main.html so it works on whole website

// Add to Cart from Products Listing i.e. Discount Products / New Arrival Products

import { apiHit } from "../../../static/js/apiHit.js";

const addItemToCart = async (event) => {
  // Access the clicked button
  const button = event.target;

  // Fetch the productId from the clicked button's data attribute
  const productId = button.getAttribute("data-product-id");
  const quantity = 1; // Replace with the desired quantity

  // Find the closest parent element within class "card"
  const productContainer = button.closest(".card");

  // Find the info message element within the product container
  const infoMessage = productContainer.querySelector(".info-message");

  // Update the info message for the specific product
  infoMessage.textContent = "Item added to Cart successfully";
  infoMessage.style.display = "block";

  apiHit(productId, quantity);

  setTimeout(() => {
    infoMessage.style.display = "none";
  }, 3000);
};

// All Products showcase Add to cart button'S
const add_to_cart_buttons = document.querySelectorAll(".addtocartbtns");

// Attach event listeners to all 'Add to Cart' buttons
add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addItemToCart);
});
