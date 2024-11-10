function toggleMenu(type) {
    const vegSection = document.getElementById('veg-items');
    const nonVegSection = document.getElementById('nonveg-items');
    
    if (type === 'veg') {
        vegSection.classList.remove('hidden');
        nonVegSection.classList.add('hidden');
    } else {
        nonVegSection.classList.remove('hidden');
        vegSection.classList.add('hidden');
    }
}

// function viewProfile() {
//     alert("Profile feature coming soon!");
// }

// function viewOrders() {
//     alert("Order tracking coming soon!");
// }

document.addEventListener("DOMContentLoaded", function () {
    const profileButton = document.getElementById("profileButton");
    const profileSection = document.getElementById("profileSection");

    profileButton.addEventListener("click", function () {
        // Toggle the 'hidden' class to show/hide the profile section
        profileSection.classList.toggle("hidden");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const profileButton = document.getElementById("profileButton");
    const profileSection = document.getElementById("profileSection");
    const loginButton = document.getElementById("loginButton");
    const loginSection = document.getElementById("loginSection");

    // Toggle Profile Section
    profileButton.addEventListener("click", function () {
        profileSection.classList.toggle("hidden");
    });

    // Toggle Login Section
    loginButton.addEventListener("click", function () {
        loginSection.classList.toggle("hidden");
    });
});
