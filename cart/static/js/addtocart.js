// This JS is LINKED to layout/Main.html so it works on whole website

// Function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Hits the API that Adds item to cart
const addtocart_api_hit = async (productId, quantity) => {
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

// ------------------MULTIPLE Products MAP Add to CART---BEGINS----------------
const addItemToCart = async (event) => {
  // Access the clicked button
  const button = event.target;

  // Fetch the productId from the clicked button's data attribute
  const productId = button.getAttribute("data-product-id");
  const quantity = 1; // Replace with the desired quantity

  addtocart_api_hit(productId, quantity);
};

// All Products showcase Add to cart button'S
const add_to_cart_buttons = document.querySelectorAll(".addtocartbtns");

// Attach event listeners to all 'Add to Cart' buttons
add_to_cart_buttons.forEach((button) => {
  button.addEventListener("click", addItemToCart);
});

// ------------------INDIVIDUAL Products Add to CART---BEGINS----BULK Quantity------------

// Individual Product Detail Page fetches multiple Qty units
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

  const infoMessage = document.getElementById("infoMessage");
  if (total_Quantity > total_Quantity_left) {
    infoMessage.textContent = `Quantity cannot exceed ${total_Quantity_left},Out of Stock!`;
    infoMessage.style.display = "block"; // Show the message
  } else if (total_Quantity <= 0) {
    infoMessage.textContent = `Minimum quantity is less than 1`;
    infoMessage.style.display = "block"; // Show the message
  } else {
    infoMessage.style.display = "none"; // Hide the message
    addtocart_api_hit(productId, total_Quantity);
  }
};

// Individual Product Page , add to cart button
const add_to_cart_button = document
  .getElementById("addtocartbtn")
  .addEventListener("click", addItemToCart_Quantity);
