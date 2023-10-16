// This JS is LINKED to layout/Main.html so it works on whole website

// Add to Cart from Products Listing i.e. Discount Products / New Arrival Products

import { addToCartAPI } from "../../../static/js/apiAddToCart.js";
import { getTotalCartCounterAPI } from "../../../static/js/apiGetTotalCartCounter.js";

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

  const data = await addToCartAPI(productId, quantity);

  // Update the info message for the specific product
  infoMessage.style.display = "block";

  // Display backend jsonresponse message
  if (data.success == true) {
    infoMessage.style.color = "Green";
    infoMessage.textContent = data.message;
    await getTotalCartCounterAPI();
  } else {
    infoMessage.style.color = "Red";
    infoMessage.textContent = data.message;
  }

  setTimeout(() => {
    infoMessage.style.display = "none";
  }, 2000);
};

// All Products showcase Add to cart button'S
const add_to_cart_buttons = document.querySelectorAll(".addtocartbtns");

// Attach event listeners to all 'Add to Cart' buttons
add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addItemToCart);
});
