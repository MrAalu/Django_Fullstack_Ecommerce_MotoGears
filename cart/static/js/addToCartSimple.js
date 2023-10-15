// This JS is LINKED to layout/Main.html so it works on whole website

// Add to Cart from Products Listing i.e. Discount Products / New Arrival Products

import { apiHit } from "../../../static/js/apiHit.js";

const addItemToCart = async (event) => {
  // Access the clicked button
  const button = event.target;

  // Fetch the productId from the clicked button's data attribute
  const productId = button.getAttribute("data-product-id");
  const quantity = 1; // Replace with the desired quantity

  apiHit(productId, quantity);
};

// All Products showcase Add to cart button'S
const add_to_cart_buttons = document.querySelectorAll(".addtocartbtns");

// Attach event listeners to all 'Add to Cart' buttons
add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addItemToCart);
});
