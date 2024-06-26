document.getElementById('upload-form').onsubmit = function(event) { // When the form with id 'upload-form' is submitted, execute this function
    event.preventDefault(); // Prevent the default form submission behavior
    let formData = new FormData(this); // Create a new FormData object, passing the form as the context ('this' refers to the form)

    fetch('/upload', { // Send a POST request to the '/upload' endpoint
        method: 'POST', // Specify the request method as POST
        body: formData // Set the request body to the FormData object
    })
    .then(response => response.blob()) // Convert the response to a Blob object
    .then(blob => { // When the Blob object is ready, execute this function
        let link = document.createElement('a'); // Create a new anchor element
        link.href = window.URL.createObjectURL(blob); // Create a URL for the Blob object and set it as the href of the anchor element
        link.download = 'allocation.csv'; // Set the download attribute of the anchor element to specify the filename
        link.click(); // Programmatically click the anchor element to trigger the download
    })
    .catch(error => console.error('Error:', error)); // If there's an error, log it to the console
};
