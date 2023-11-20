// Handles Shipping Details FORM in Checkout.html Page

import { getCookie } from "./getCookie.js";

export const handleShippingFormAPI = async (formObject) => {
  try {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.post(
      `http://127.0.0.1:8000/checkout/api/handle-shipping-form/`,
      { formObject },
      {
        headers: {
          "X-CSRFToken": csrfToken,
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );

    const data = await response.data;
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
};
