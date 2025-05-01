document.addEventListener('DOMContentLoaded', function() {
    // Select all download links (file items)
    const downloadLinks = document.querySelectorAll('.download-link');

    downloadLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();  // Prevent default behavior

            // Get the file ID from the data attribute
            const fileId = link.getAttribute('data-file-id');
            
            // Show the modal
            const modal = document.getElementById('password-modal');
            modal.style.display = 'block';

            // Handle submit password button click
            document.getElementById('submit-password').addEventListener('click', function() {
                const password = document.getElementById('file-password').value;
                
                // Send the password to the server via POST
                fetch(`/file/download/${fileId}/`, {
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
                        alert("Invalid password or an error occurred.");
                        return;
                    }

                    return response.blob();  // Convert the response to a blob (binary data)
                })
                .then(blob => {
                    if (blob) {
                        // Create a download link and trigger the download
                        const link = document.createElement('a');
                        const downloadUrl = window.URL.createObjectURL(blob);
                        link.href = downloadUrl;
                        link.download = `file_${fileId}`;  // You can modify this filename as needed
                        link.click();
                        modal.style.display = 'none';  // Hide the modal after download
                    }
                })
                .catch(error => {
                    console.error("Download failed:", error);
                    alert("Error occurred during file download.");
                });
            });
        });
    });
});
