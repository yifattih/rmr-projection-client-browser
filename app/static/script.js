$(document).ready(function() {
    // Load existing data
    // loadDataIn();

    //////// Show initial message ////////

    var statusMessageContainer = $("header h5");
    displayMessage(
        statusMessageContainer,
        "App: Ready!"
    );

    //////// Input data validation ////////

    // Age must be 19 years or more
    var ageField = $("#input-age");
    var minAge = 19;
    var ageErrorMessage = "Age must be 19 years or more";
    checkIfGreaterThan(
        ageField,
        minAge,
        ageErrorMessage,
        statusMessageContainer
    );
    
    // Initial weight mus be 0 or more
    var weightField = $('#input-weight');
    var minWeight = 0;
    var weightErrorMessage = "Weight must be 0 or more";
    checkIfGreaterThan(
        weightField,
        minWeight,
        weightErrorMessage,
        statusMessageContainer
    );

    // Height must be 0 or more
    var heightField = $('#input-height');
    var minHeight = 0;
    var heightErrorMessage = "Height must be 0 or more";
    checkIfGreaterThan(
        heightField,
        minHeight,
        heightErrorMessage,
        statusMessageContainer
    );

    //////// Change units based on selection ////////

    $('#select-units').on(
        'change',
        function() {
            // Code to execute when the select option changes
            var selectedValue = $(this).val();
            if (selectedValue == 'imperial') {
                $('#label-weight-unit').text("lbs")
                $('#label-rate-unit').text("lbs")
                $('#label-height-unit').text("inch")
            } else {
                $('#label-weight-unit').text("kg")
                $('#label-rate-unit').text("kg")
                $('#label-height-unit').text("cm")
            };
        }
    );

    //////// Handle form submission ////////

    $('#data-form').on(
        'submit',
        function(event) {
        event.preventDefault();
        var form_data = $('#data-form').serializeArray();
        console.log(form_data);
        for (var input in form_data){
            var element=$("#input-"+form_data[input]['name']);
            console.log(element);
        };
        const sex = $('#select-sex').val();
        const age = $('#input-age').val();
        const weight = $('#input-weight').val();
        const height = $('#input-height').val();
        const units = $('#select-units').val();
        const weeks = $('#input-time').val();
        const weightLossRate = $('#input-rate').val();
        const energyDeficit = $('#input-energy').val();

        $.ajax({
            url: '/model',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                sex: sex,
                age: age,
                weight: weight,
                height: height,
                units: units,
                weeks: weeks,
                weight_loss_rate: weightLossRate,
                energy_deficit: energyDeficit
            }),
            success: function(response) {
                console.log("Server response");
                console.log(response);
                serverMessage = `${response.message}: ${response.status}`;
                displayMessage(statusMessageContainer, serverMessage);

                // $('.data-log').append(`<p>Sex: ${response.data_out.sex}</p>`);
                // $('.data-log').append(`<p>Age: ${response.data_out.age} years</p>`);
                // $('.data-log').append(`<p>Weight: ${response.data_out.weight} lbs</p>`);
                // $('.data-log').append(`<p>Height: ${response.data_out.height} inches</p>`);
                // $('.data-log').append(`<p>Units: ${response.data_out.units}</p>`);
                // $('.data-log').append(`<p>Equations: ${response.data_out.equations}</p>`);
                // $('.data-log').append(`<p>Weeks: ${response.data_out.weeks}</p>`);
                // $('.data-log').append(`<p>Weight Loss Rate: ${response.data_out.weight_loss_rate} lbs</p>`);
                // $('.data-log').append(`<p>Energy Deficit: ${response.data_out.energy_deficit} cal</p>`);
                // $('.data-log').append(`<p>Time Projected: ${response.data_out.time_projected} weeks</p>`);
                // $('.data-log').append(`<p>BMR to Keep Weight: ${response.data_out.bmr} cal</p>`);
                // $('.data-log').append(`<p>BMR to Loose 2 Pounds: ${response.data_out.bmr_deficit} cal</p>`);
            }
        });
    });

    //////// Handle form clearing ////////

    $('.clear').on(
        'click',
        function(event) {
        event.preventDefault();
        $.ajax({
            url: '/reset',
            type: 'POST',
            contentType: 'application/json',
            success: function(response) {
                console.log("Server response");
                console.log(response);
                serverMessage = `${response.message}: ${response.status}`;
                displayMessage(statusMessageContainer, serverMessage);
                // Clear form fields
                $('#input-age').val('');
                $('#input-weight').val('');
                $('#input-height').val('');
                $('#input-time').val('');
                $('#input-rate').val('2');
                $('#input-energy').val('1000');
            }
        });
    });
});

//////// Utility functions ////////

function checkIfGreaterThan (
    field,
    minValue,
    errorMessage,
    messageContainer) {
    field.on(
        'blur',
        function() {
        var input = $(this);
        var inputValue = input.val();

        if(inputValue >= minValue) {
            input.removeClass("input-invalid").addClass("input-valid");
            messageContainer.removeClass("input-invalid").addClass("input-valid");
        }
        else {
            input.removeClass("input-valid").addClass("input-invalid");
            messageContainer.removeClass("input-valid").addClass("input-invalid");
            // Append the error message and show
            displayMessage(messageContainer, errorMessage);
            // Remove the error message on focus
            input.on("focus", function() {
                errorMessage = "";
            });
        };
    });
};

function displayMessage (messageContainer, message) {
    messageContainer.empty();
    messageContainer.append(message);

    messageContainer.animate(
        {"opacity": 100},
        700
    );

    messageContainer.animate(
        {"opacity": 0},
        900
    );
};

// function loadDataIn() {
//     $.ajax({
//         url: '/data-in',
//         type: 'GET',
//         success: function(data_in) {
//             data_in.forEach(item => {
//                 $('#dataTable tbody').append(`<tr><td>${item.weight}</td><td>${item.height}</td><td>${item.age}</td><td>${item.time}</td></tr>`);
//             });
//         }
//     });
// }

// function loadDataOut() {
//     $.ajax({
//         url: '/data-out',
//         type: 'GET'
//         })
// }