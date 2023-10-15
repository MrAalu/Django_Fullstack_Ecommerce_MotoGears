// This JS is LINKED to layout/Main.html so it works on whole website

// Add to Cart products with Multiple Quantities from Product Detail/Individual Page or Cart Page

import { apiHit } from "../../../static/js/apiHit.js";

const addItemToCart_Quantity = async (event) => {
  event.preventDefault();
  // Access the clicked button
  const button = event.target;

  // Fetch the productId from the clicked button's data attribute
  const productId = button.getAttribute("data-product-id");
  const total_Quantity = Number(
    document.getElementById("cart_item_quantity").value
  );

  // Total available Quantity
  const total_Quantity_left = Number(
    document.getElementById("cart_item_quantity").getAttribute("max")
  );

  // Input Field Validation Message
  const infoMessage = document.getElementById("infoMessage");
  if (total_Quantity > total_Quantity_left) {
    infoMessage.textContent = `Quantity cannot exceed ${total_Quantity_left},Out of Stock!`;
    infoMessage.style.display = "block"; // Show the message
  } else if (total_Quantity <= 0) {
    infoMessage.textContent = `Minimum quantity is 1`;
    infoMessage.style.display = "block"; // Show the message
  } else {
    infoMessage.style.display = "none"; // Hide the message
    apiHit(productId, total_Quantity);
  }
};

// Individual Product Page , add to cart button
const add_to_cart_button = document.getElementById("addtocartbtn");
if (add_to_cart_button) {
  add_to_cart_button.addEventListener("click", addItemToCart_Quantity);
}
