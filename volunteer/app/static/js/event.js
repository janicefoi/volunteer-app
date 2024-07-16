// Function to show signup modal
function showSignupModal(eventId) {
    var modal = document.getElementById('signupModal');
    modal.style.display = "block";
    // Store eventId in a hidden field or global variable to use in signupForEvent function
    document.getElementById('eventIdField').value = eventId;
}

// Function to close signup modal
function closeSignupModal() {
    var modal = document.getElementById('signupModal');
    modal.style.display = "none";
}

// Function to confirm signup
function confirmSignup() {
    // Hide the initial signup modal
    closeSignupModal();

    // Show the confirmation dialog
    var confirmationDialog = document.getElementById('confirmationDialog');
    confirmationDialog.style.display = "block";

    // Handle confirmation actions
    document.getElementById('confirmYes').onclick = function() {
        var eventId = document.getElementById('eventIdField').value;
        fetch(`/signup/${eventId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            alert(data.message);
            // You may want to update UI or reload the page after signup
            location.reload(); // Example: reload page after signup
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred, please try again later.');
        })
        .finally(() => {
            // Close the confirmation dialog
            confirmationDialog.style.display = "none";
        });
    };

    // Handle cancellation action
    document.getElementById('confirmNo').onclick = function() {
        // Close the confirmation dialog without taking action
        confirmationDialog.style.display = "none";
    };
}

// Function to close signup modal
function closeSignupModal() {
    var modal = document.getElementById('signupModal');
    modal.style.display = "none";
}


// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
