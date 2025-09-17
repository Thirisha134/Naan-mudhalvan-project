<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Intelligent Citizen Engagement Platform</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f0f8ff;
    }
    h2 {
      color: #2c3e50;
    }
    .hidden {
      display: none;
    }
    .container {
      max-width: 500px;
      margin: auto;
      background: #ffffff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      margin-top: 10px;
      font-size: 1em;
    }
    .logout-btn {
      background-color: #e74c3c;
      color: white;
      border: none;
      margin-top: 20px;
    }
    .submit-btn {
      background-color: #3498db;
      color: white;
      border: none;
    }
  </style>
</head>
<body>

  <div class="container" id="loginForm">
    <h2>Login</h2>
    <input type="text" id="username" placeholder="Username">
    <input type="password" id="password" placeholder="Password">
    <button onclick="login()">Login</button>
  </div>

  <div class="container hidden" id="citizenForm">
    <h2>Citizen Information</h2>
    <input type="text" id="name" placeholder="Full Name">
    <input type="number" id="age" placeholder="Age">
    <input type="text" id="city" placeholder="City">
    <select id="service">
      <option value="">Select a Service</option>
      <option value="Water Supply Issue">Water Supply Issue</option>
      <option value="Electricity Complaint">Electricity Complaint</option>
      <option value="Garbage Collection">Garbage Collection</option>
      <option value="Road Repair Request">Road Repair Request</option>
    </select>
    <button class="submit-btn" onclick="submitForm()">Submit</button>
    <button class="logout-btn" onclick="logout()">Logout</button>
  </div>

  <div class="container hidden" id="confirmation">
    <h2>? Submission Successful</h2>
    <p><strong>Name:</strong> <span id="displayName"></span></p>
    <p><strong>Age:</strong> <span id="displayAge"></span></p>
    <p><strong>City:</strong> <span id="displayCity"></span></p>
    <p><strong>Requested Service:</strong> <span id="displayService"></span></p>
    <button class="logout-btn" onclick="logout()">Logout</button>
  </div>

  <script>
    const validUser = { username: "citizen", password: "1234" }; // Mock credentials

    function login() {
      const uname = document.getElementById("username").value;
      const pwd = document.getElementById("password").value;

      if (uname === validUser.username && pwd === validUser.password) {
        sessionStorage.setItem("loggedIn", "true");
        document.getElementById("loginForm").classList.add("hidden");
        document.getElementById("citizenForm").classList.remove("hidden");
      } else {
        alert("? Invalid credentials. Try 'citizen' / '1234'.");
      }
    }

    function submitForm() {
      const name = document.getElementById("name").value;
      const age = document.getElementById("age").value;
      const city = document.getElementById("city").value;
      const service = document.getElementById("service").value;

      if (!name || !age || !city || !service) {
        alert("? Please fill in all fields.");
        return;
      }

      document.getElementById("displayName").textContent = name;
      document.getElementById("displayAge").textContent = age;
      document.getElementById("displayCity").textContent = city;
      document.getElementById("displayService").textContent = service;

      document.getElementById("citizenForm").classList.add("hidden");
      document.getElementById("confirmation").classList.remove("hidden");
    }

    function logout() {
      sessionStorage.removeItem("loggedIn");
      document.getElementById("loginForm").classList.remove("hidden");
      document.getElementById("citizenForm").classList.add("hidden");
      document.getElementById("confirmation").classList.add("hidden");

      // Clear form fields
      document.querySelectorAll("input, select").forEach(el => el.value = "");
    }

    // Auto-redirect if already logged in
    window.onload = () => {
      if (sessionStorage.getItem("loggedIn") === "true") {
        document.getElementById("loginForm").classList.add("hidden");
        document.getElementById("citizenForm").classList.remove("hidden");
      }
    };
  </script>
</body>
</html>