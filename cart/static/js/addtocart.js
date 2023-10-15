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

const addItemToCart = async (event) => {
  // Access the clicked button
  const button = event.target;

  // Fetch the productId from the clicked button's data attribute
  const productId = button.getAttribute("data-product-id");
  const quantity = 1; // Replace with the desired quantity

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
    console.log(response);
    const data = response.data;

    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
};

// Get all elements with the 'addtocartbtn' class
const addButtons = document.querySelectorAll(".addtocartbtn");

// Attach event listeners to all 'Add to Cart' buttons
addButtons.forEach((button) => {
  button.addEventListener("click", addItemToCart);
});
