const imageUpload = document.getElementById('imageUpload');
const submitButton = document.getElementById('submitButton');

// submit button unlocked 
imageUpload.addEventListener('change', function() {
    if (imageUpload.files.length > 0) {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
});
