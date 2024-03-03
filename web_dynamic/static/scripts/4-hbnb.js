$(document).ready(function() {
    // Add click event listener to button tag
    $('button').click(function() {
        // Define list of amenities checked
        var amenitiesChecked = [];

        // Loop through each checkbox and add checked amenities to the list
        $('input[type="checkbox"]:checked').each(function() {
            amenitiesChecked.push($(this).data('id'));
        });

        // Make a POST request to places_search with the list of amenities checked
        $.ajax({
            type: 'POST',
            url: 'http://0.0.0.0:5001/api/v1/places_search',
            contentType: 'application/json',
            data: JSON.stringify({ amenities: amenitiesChecked }),
            success: function(response) {
                // Handle success response
                console.log('POST request successful:', response);
            },
            error: function(xhr, status, error) {
                // Handle error response
                console.error('Error making POST request:', error);
            }
        });
    });
});
