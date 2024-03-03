$(document).ready(function() {
    $('#toggle-reviews').click(function() {
        var $toggleSpan = $(this);
        if ($toggleSpan.text() === 'show') {
            // Fetch, parse, and display reviews
            // Example: $.get('reviews_endpoint', function(data) { /* parse and display reviews */ });
            $toggleSpan.text('hide');
        } else {
            // Hide reviews
            // Example: $('.review').remove();
            $toggleSpan.text('show');
        }
    });
});
