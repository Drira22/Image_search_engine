const imageUpload = document.getElementById('imageupload');
const submitButton = document.getElementById('submitButton');
const previewContainer = document.getElementById('previewContainer');
const imagePreview = document.createElement('img');

previewContainer.appendChild(imagePreview);

imageUpload.addEventListener('change', function () {
    submitButton.disabled = imageUpload.files.length === 0;

    if (imageUpload.files.length > 0) {
        const file = imageUpload.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };

        reader.readAsDataURL(file);
    } else {
        imagePreview.style.display = 'none';
    }
});

submitButton.addEventListener('click', function () {
    const title = document.querySelector('h3');
    title.style.display = 'block'; // Show the title


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
