// file_download.js - Enhanced functionality for the file listing page

document.addEventListener('DOMContentLoaded', function() {
  // Enhance the file list items with proper structure and classes
  const fileItems = document.querySelectorAll('li');
  
  fileItems.forEach(item => {
    // Get the existing elements
    const link = item.querySelector('a');
    const dateInfo = item.innerHTML.match(/\(Uploaded at: .*?\)/);
    const form = item.querySelector('form');
    
    // Clear the item's content
    const originalContent = item.innerHTML;
    item.innerHTML = '';
    
    // Create file info container
    const fileInfo = document.createElement('div');
    fileInfo.className = 'file-info';
    
    // Add file name with proper formatting
    const fileName = document.createElement('div');
    fileName.className = 'file-name';
    fileName.appendChild(link);
    
    // Add date info
    const fileDate = document.createElement('div');
    fileDate.className = 'file-date';
    fileDate.textContent = dateInfo ? dateInfo[0] : '';
    
    // Assemble the structure
    fileInfo.appendChild(fileName);
    fileInfo.appendChild(fileDate);
    
    // Add the structured elements back to the list item
    item.appendChild(fileInfo);
    item.appendChild(form);
    
    // Add file type-specific classes based on the filename
    const fileExtension = getFileExtension(link.textContent);
    if (fileExtension) {
      link.classList.add(`file-${fileExtension.toLowerCase()}`);
    }
    
    // Add animation for newly added files (based on timestamp)
    const uploadDate = extractUploadDate(dateInfo ? dateInfo[0] : '');
    if (isRecentlyUploaded(uploadDate)) {
      item.classList.add('new-file');
    }
  });
  
  // Add password visibility toggle functionality
  const passwordInputs = document.querySelectorAll('input[type="password"]');
  passwordInputs.forEach(input => {
    // Create toggle button
    const toggleBtn = document.createElement('button');
    toggleBtn.type = 'button';
    toggleBtn.className = 'password-toggle';
    toggleBtn.textContent = 'Show';
    toggleBtn.style.marginLeft = '10px';
    toggleBtn.style.padding = '5px 10px';
    toggleBtn.style.background = 'transparent';
    toggleBtn.style.border = '1px solid #ccc';
    toggleBtn.style.borderRadius = '4px';
    toggleBtn.style.cursor = 'pointer';
    
    toggleBtn.addEventListener('click', function() {
      // Toggle password visibility
      if (input.type === 'password') {
        input.type = 'text';
        toggleBtn.textContent = 'Hide';
      } else {
        input.type = 'password';
        toggleBtn.textContent = 'Show';
      }
    });
    
    // Add the toggle button after the input
    input.parentNode.insertBefore(toggleBtn, input.nextSibling);
  });
});

// Helper function to extract file extension
function getFileExtension(filename) {
  const match = filename.match(/\.([a-zA-Z0-9]+)$/);
  return match ? match[1] : null;
}

// Helper function to extract upload date from the string
function extractUploadDate(dateString) {
  const match = dateString.match(/(\d{4}-\d{2}-\d{2} \d{2}:\d{2})/);
  return match ? new Date(match[1]) : null;
}

// Helper function to check if a file was uploaded recently (within the last 24 hours)
function isRecentlyUploaded(uploadDate) {
  if (!uploadDate) return false;
  
  const now = new Date();
  const diffTime = now - uploadDate;
  const diffHours = diffTime / (1000 * 60 * 60);
  
  return diffHours < 24;
}