$(document).ready(function() {
    // Listen for changes on state checkboxes
    $('#states input[type="checkbox"]').change(function() {
        updateSelectedLocations();
    });

    // Listen for changes on city checkboxes
    $('#cities input[type="checkbox"]').change(function() {
        updateSelectedLocations();
    });

    // Function to update selected locations
    function updateSelectedLocations() {
        var selectedLocations = [];

        // Add selected states to the list
        $('#states input[type="checkbox"]:checked').each(function() {
            var id = $(this).data('id');
            var name = $(this).data('name');
            selectedLocations.push(name + ' (ID: ' + id + ')');
        });

        // Add selected cities to the list
        $('#cities input[type="checkbox"]:checked').each(function() {
            var id = $(this).data('id');
            var name = $(this).data('name');
            selectedLocations.push(name + ' (ID: ' + id + ')');
        });

        // Update the display with selected locations
        $('#selected-locations p').text(selectedLocations.length > 0 ? selectedLocations.join(', ') : 'No locations selected');
    }
});
