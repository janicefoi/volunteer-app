document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('volunteerForm');
    const photoSelect = document.getElementById('photo');
    const photoUploadGroup = document.getElementById('photoUploadGroup');
    
    photoSelect.addEventListener('change', function() {
        if (this.value === 'yes') {
            photoUploadGroup.style.display = 'block';
        } else {
            photoUploadGroup.style.display = 'none';
        }
    });
    
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
            alert(data.message);
            form.reset(); // Optionally reset the form after submission
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
