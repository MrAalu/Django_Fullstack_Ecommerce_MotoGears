// API to Update Cart Items Quantity from Cart.html

import { getCookie } from "./getCookie.js";

export const updateCartQuantityAPI = async (productId, new_Quantity) => {
  try {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.post(
      `http://127.0.0.1:8000/cart/api/update-cart-quantity/`,
      {
        product_id: productId,
        new_Quantity: new_Quantity,
      },
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
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
};
