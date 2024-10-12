$(document).ready(function() {
    // Load existing data
    loadData();

    // Handle form submission
    $('#dataForm').on('submit', function(event) {
        event.preventDefault();

        const weight = $('#weight').val();
        const height = $('#height').val();
        const age = $('#age').val();
        const time = $('#time').val();

        $.ajax({
            url: '/calculate',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ weight: weight, height: height, age: age, time: time }),
            success: function(data) {
                $('#dataTable tbody').empty();
                data.forEach(item => {
                    $('#dataTable tbody').append(`<tr><td>${item.weight}</td><td>${item.height}</td><td>${item.age}</td><td>${item.time}</td></tr>`);
                });
            }
        });
        
        // Clear form fields
        $('#weight').val('');
        $('#height').val('');
        $('#age').val('');
        $('#time').val('');
    });

    $('#dataForm').on('reset', function(event) {
        event.preventDefault();
        
        $.ajax({
            url: '/clear',
            type: 'POST',
            contentType: 'application/json',
            success: function() {
                $('#dataTable tbody').empty();
            }
        });
    });
});

function loadData() {
    $.ajax({
        url: '/data',
        type: 'GET',
        success: function(data) {
            data.forEach(item => {
                $('#dataTable tbody').append(`<tr><td>${item.weight}</td><td>${item.height}</td><td>${item.age}</td><td>${item.time}</td></tr>`);
            });
        }
    });
}