// donations.js

// Function to show the donation modal and set the donation ID
function showDonationModal(donationId) {
    document.getElementById('donationModal').style.display = 'block';
    document.getElementById('donationIdField').value = donationId;
}

// Function to close the donation modal
function closeDonationModal() {
    document.getElementById('donationModal').style.display = 'none';
    clearMessages();
}

// Function to clear success and error messages
function clearMessages() {
    document.getElementById('successMessage').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
}

// Function to submit the donation
function submitDonation() {
    const amount = document.getElementById('amount').value;
    const phoneNumber = document.getElementById('phone_number').value;
    const donationId = document.getElementById('donationIdField').value;

    if (!amount || !phoneNumber) {
        document.getElementById('errorMessage').innerText = 'Please fill out all fields.';
        document.getElementById('errorMessage').style.display = 'block';
        return;
    }

    const data = {
        amount: amount,
        phone_number: phoneNumber,
        donation_id: donationId
    };

    fetch('/initiate_mpesa_payment/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('successMessage').style.display = 'block';
        } else {
            document.getElementById('errorMessage').innerText = data.message || 'Payment failed. Please try again.';
            document.getElementById('errorMessage').style.display = 'block';
        }
    })
    .catch(error => {
        document.getElementById('errorMessage').innerText = 'An error occurred. Please try again.';
        document.getElementById('errorMessage').style.display = 'block';
    });
}

// Utility function to get the CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
