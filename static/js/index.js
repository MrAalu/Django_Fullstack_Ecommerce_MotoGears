// This JS is LINKED to layout/Main.html so it works on whole website

// Fetches Cookie with given name
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Generate a Unique Device ID
function uuidv4() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c == "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

let device = getCookie("device");

if (device == null || device == undefined) {
  device = uuidv4();
}

// Sets the Cookie
document.cookie = "device=" + device + ";domain=;path=/";

// Summary : We are generating a Unique Device id for Guest users to keep track of their CART items which then later, on Checkout process or if the user logs in , then we will MERGE this CART with user's Account !
