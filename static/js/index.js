// This JS is LINKED to layout/Main.html so it works on whole website

import { getCookie } from "./getCookie.js";
import { getDeviceId } from "./getDeviceID.js";

let device = getCookie("device");

// If user doesnt have a Device ID then generates one and sets the Cookie
if (device == null || device == undefined) {
  device = getDeviceId();
}
// Sets the Cookie
document.cookie = "device=" + device + ";domain=;path=/";

// Summary : We are generating a Unique Device id for Guest users to keep track of their CART items which then later, on Checkout process or if the user logs in , then we will MERGE this CART with user's Account !
