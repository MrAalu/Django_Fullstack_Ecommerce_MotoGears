// This JS is LINKED to layout/Main.html so it works on whole website

import { getCookie } from "./getCookie.js";
import { getDeviceId } from "./getDeviceID.js";

let device = getCookie("device");

// If user doesnt have a Device ID then generates one and sets the Cookie
if (device == null || device == undefined) {
  device = getDeviceId();
}

// create expiry date for cookie
// 86400 = 24hours in ms * 1000  = 1day
var expires = new Date(Date.now() + 86400 * 1000 * 30).toUTCString();

// Set the cookie with the updated expiration date
document.cookie = "device=" + device + "; expires=" + expires + "; path=/";

// When DeviceID cookie is created ,its given 30days expiry time which will be stored as Value to 'cart_expiry' cookie to display the cart expiry date on Cart page for Guest users
document.cookie = "cart_expiry=" + expires;

// Summary : We are generating a Unique Device id for Guest users to keep track of their CART items which then later, on Checkout process or if the user logs in , then we will MERGE this CART with user's Account !
