// Hits the API that Adds item to cart

import { getCookie } from "./getCookie.js";

export const apiHit = async (productId, quantity) => {
  try {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.post(
      `http://127.0.0.1:8000/cart/add-to-cart/`,
      {
        product_id: productId,
        quantity: quantity,
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
    const data = response.data;

    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
};
