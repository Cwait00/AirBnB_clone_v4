document.addEventListener('DOMContentLoaded', function () {
    // Send POST request to fetch places
    fetch('http://0.0.0.0:5001/api/v1/places_search/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        // Loop through the results and create article tags for each place
        data.forEach(place => {
            // Create article tag and populate with place information
            let article = document.createElement('article');
            article.innerHTML = `
                <h2>${place.name}</h2>
                <!-- Add more place information here as needed -->
            `;

            // Append article tag to section.places
            document.querySelector('section.places').appendChild(article);
        });
    })
    .catch(error => console.error('Error fetching places:', error));
});
