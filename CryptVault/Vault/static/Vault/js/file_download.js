document.addEventListener('DOMContentLoaded', function () {
    let currentFileId = null;

    const downloadLinks = document.querySelectorAll('.download-link');
    const modal = document.getElementById('password-modal');
    const submitBtn = document.getElementById('submit-password');
    const passwordInput = document.getElementById('file-password');

    // Attach click listeners to each download link
    downloadLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            currentFileId = link.getAttribute('data-file-id');
            passwordInput.value = '';  // Clear previous input
            modal.style.display = 'block';
        });
    });

    // Attach one listener to the submit button
    submitBtn.addEventListener('click', function () {
        const password = passwordInput.value;
        if (!currentFileId || !password) {
            alert("Password is required.");
            return;
        }

        fetch(`/file/download/${currentFileId}/`, {
            method: 'POST',
            body: new URLSearchParams({
                'password': password
            }),
            headers: {
                'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Invalid password or download error.");
            }
            return response.blob();
        })
        .then(blob => {
            if (blob) {
                const downloadUrl = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = downloadUrl;
                a.download = `file_${currentFileId}`; // Set the filename as needed
                document.body.appendChild(a);
                a.click();
                a.remove();
                modal.style.display = 'none';
            }
        })
        .catch(error => {
            console.error("Download failed:", error);
            alert("Error occurred during file download.");
        });
    });
});
