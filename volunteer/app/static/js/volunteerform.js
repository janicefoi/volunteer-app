document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('volunteerForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            // Show the modal with the success message
            $('#successModal').modal('show');
            form.reset(); // Optionally reset the form after submission
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
