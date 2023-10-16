// If user if not logged in and user is using cart as GuestUser then after the DeviceID cookie is expired the cart will be removed

// Fetching DeviceID cookie expiry time and display to user

// Future TODO Feature : Automatic deleting guest users cart after 30days to free up database

import { getCookie } from "../../../static/js/getCookie.js";

const cart_expiry_cookie_value = getCookie("cart_expiry");

const cartExpiryDate = document.getElementById("cart-expiry-date");

if (cartExpiryDate) {
  const originalDate = new Date(cart_expiry_cookie_value);
  const options = {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "numeric",
  };
  const formattedDate = originalDate.toLocaleDateString("en-US", options);

  cartExpiryDate.textContent = formattedDate;
}
