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
        
        // Here you can add form validation or submission logic
        console.log('Form submitted');
        
        // Example of form data collection
        const formData = new FormData(form);
        for (let [key, value] of formData.entries()) {
            console.log(key + ': ' + value);
        }
        
        // You might want to send this data to a server here
        // For now, we'll just alert the user
        alert('Thank you for volunteering! Your information has been submitted.');
    });
});