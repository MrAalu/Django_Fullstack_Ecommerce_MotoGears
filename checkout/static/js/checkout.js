import { handleShippingFormAPI } from "../../../static/js/apiShipping.js";

const shipping_form = document.getElementById("shipping-form");
const payment_form = document.getElementById("payment-form");

if (shipping_form) {
  // handles Shipping form submission
  shipping_form.addEventListener("submit", async function (e) {
    e.preventDefault();

    // Get form data
    const formData = new FormData(shipping_form);

    // Convert FormData to a plain JavaScript object
    const formObject = {};
    formData.forEach((value, key) => {
      formObject[key] = value;
    });

    // Validate phone number before making post request of shipping details (Phone number must be 10digits)
    const phone_number = formObject["phone_number"];
    const isPhoneNumberValid = validatePhoneNumber(phone_number);

    // If phone number is not Valid then,Display the red prompt
    if (!isPhoneNumberValid) {
      const info_message = document.getElementById("info-message");
      info_message.style.display = "block";
      info_message.style.color = "Red";
      info_message.textContent =
        "Phone number must be 10digits and should start with '9...'";
      console.error("Invalid Phone Number");

      setTimeout(() => {
        info_message.style.display = "none";
      }, 2500);
    } else {
      // Disabling 'Continue' button (Shipping Form)
      const btn_shipping_form = document.getElementById("btn-shipping-form");
      btn_shipping_form.disabled = true;
      btn_shipping_form.textContent = "Loading...";

      // Call your API handling function
      const data = await handleShippingFormAPI(formObject);

      if (data?.success == true) {
        btn_shipping_form.disabled = false;
        payment_form.style.display = "block";
        shipping_form.style.display = "none";
      }
    }
  });
}

// Function to validate phone number on Shipping details FORM
function validatePhoneNumber(phone_number) {
  // Phone number should start with '9' and must be 10digts
  const phoneNumberRegex = /^9\d{9}$/;
  const isPhoneNumberValid = phoneNumberRegex.test(phone_number);
  return isPhoneNumberValid;
}
