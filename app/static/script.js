$(document).ready(function() {
    // Load existing data
    loadDataIn();

    // Handle form submission
    $('#dataForm').on('submit', function(event) {
        event.preventDefault();

        const weight = $('#weight').val();
        const height = $('#height').val();
        const age = $('#age').val();
        const time = $('#time').val();

        $.ajax({
            url: '/model-construct',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ weight: weight,
                height: height,
                age: age,
                time: time }),
            success: function(response) {
                console.log("Server response")
                console.log(response)
                $('#inputDataTable tbody').empty();
                $('#outputDataTable tbody').empty();
                response.data_out.forEach(item => {
                    $('#inputDataTable tbody').append(`<tr><td>${item.weight}</td><td>${item.height}</td><td>${item.age}</td><td>${item.time}</td></tr>`);
                    // Loop through data and fill table cells
                    console.log("Output lenght")
                    console.log(item.weight_loss_rate_time.length)
                    for (let i = 0; i < item.weight_loss_rate_time.length; i++) {
                        const row = $("<tr></tr>");
                        row.append($("<td></td>").text(item.weight_loss_rate_time[i]));
                        row.append($("<td></td>").text(item.weight_loss_projection[i]));
                        row.append($("<td></td>").text(item.bmr_daily[i]));
                        row.append($("<td></td>").text(item.bmr_with_deficit_daily[i]));
                        row.append($("<td></td>").text(item.bmr_total[i]));
                        row.append($("<td></td>").text(item.bmr_with_deficit_total[i]));
                        $("#outputDataTable tbody").append(row);
                    }
                });
            }
        });
        
        // Clear form fields
        // $('#weight').val('');
        // $('#height').val('');
        // $('#age').val('');
        // $('#time').val('');
    });

    $('#dataForm').on('reset', function(event) {
        event.preventDefault();
        
        $.ajax({
            url: '/reset',
            type: 'POST',
            contentType: 'application/json',
            success: function(response) {
                console.log("Server response")
                console.log(response)
                $('#inputDataTable tbody').empty();
                $('#outputDataTable tbody').empty();
            }
        });
    });
});

function loadDataIn() {
    $.ajax({
        url: '/data-in',
        type: 'GET',
        success: function(data_in) {
            data_in.forEach(item => {
                $('#dataTable tbody').append(`<tr><td>${item.weight}</td><td>${item.height}</td><td>${item.age}</td><td>${item.time}</td></tr>`);
            });
        }
    });
}

function loadDataOut() {
    $.ajax({
        url: '/data-out',
        type: 'GET'
        })
}