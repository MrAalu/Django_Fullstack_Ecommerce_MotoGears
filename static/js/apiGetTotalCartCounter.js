// Fetches total number of Carts for NAVBAR

import { getCookie } from "./getCookie.js";

export const getTotalCartCounterAPI = async () => {
  try {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.get(
      `http://127.0.0.1:8000/cart/api/cart-item-counter/`,
      {},
      {
        headers: {
          "X-CSRFToken": csrfToken,
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    // console.log(response);
    const data = await response.data;
    // console.log(data);
    const totalCartItemsCount = data.total_carts;

    // Change Cart item counter from Navbar
    const itemCounter = document.getElementById("cart-item-count");
    itemCounter.textContent = totalCartItemsCount;
  } catch (error) {
    console.error("Error:", error);
  }
};

getTotalCartCounterAPI();
