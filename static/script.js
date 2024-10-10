const imageUpload = document.getElementById('imageupload');
const submitButton = document.getElementById('submitButton');

imageUpload.addEventListener('change', function() {
    submitButton.disabled = imageUpload.files.length === 0;
});

submitButton.addEventListener('click', function() {
    const formData = new FormData();
    formData.append('file', imageUpload.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    }).then(response => response.json()).then(data => {
        const resultsContainer = document.getElementById('resultsContainer');
        resultsContainer.innerHTML = ''; // Clear previous results

        data.similarImages.forEach(image => {
            const col = document.createElement('div');
            col.className = 'col-md-4 mb-3';
            col.innerHTML = `<img src="${image.image_path}" alt="${image.image_id}" class="img-fluid" />`;
            resultsContainer.appendChild(col);
        });
    }).catch(error => {
        console.error('Error:', error);
    });
});
