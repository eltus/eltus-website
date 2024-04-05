// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-analytics.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCRAG928OhZcfPh-wl7er6JzZY2lQhRyqE",
  authDomain: "user-authentication-dddb1.firebaseapp.com",
  projectId: "user-authentication-dddb1",
  storageBucket: "user-authentication-dddb1.appspot.com",
  messagingSenderId: "333594131105",
  appId: "1:333594131105:web:955a1cac2a189aad814ee0",
  measurementId: "G-RB5V68ZCGM",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
