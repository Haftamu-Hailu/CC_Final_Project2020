(function ($) {
    apiUrl1 = 'https://9nkxihjvv1.execute-api.eu-west-1.amazonaws.com/default/CCBDAProject-SQS_And_SNS';
    apiUrl2 = 'https://fuhw6g25tb.execute-api.eu-west-1.amazonaws.com/default/CCBDAProject-RDSConnect';

    // Form submit
    $("#simulatorSetUpForm").submit(function (event) {
        event.preventDefault();
        var user_email = $("#user_email").val();
        var contact_tracing = $("#contact_tracing").val();
        var total_agents = $("#total_agents").val();
        var infected_agents = $("#infected_agents").val();
        var office_capacity = $("#office_capacity").val();
        var home_capacity = $("#home_capacity").val();
        var mortality_rate = $("#mortality_rate").val();
        var risk_home = $("#risk_home").val();
        var risk_work = $("#risk_work").val();
        var sick_days = $("#sick_days").val();
        var free_symptoms_days = $("#free_symptoms_days").val();
        var total_days = $("#total_days").val();

        var initial_data = {
            user_email: user_email,
            contact_tracing: contact_tracing,
            total_agents: total_agents,
            infected_agents: infected_agents,
            office_capacity: office_capacity,
            home_capacity: home_capacity,
            mortality_rate: mortality_rate,
            risk_home: risk_home,
            risk_work: risk_work,
            sick_days: sick_days,
            free_symptoms_days: free_symptoms_days,
            total_days: total_days
        };

        var data = {initial_data: initial_data}

        // Call API Gateway POST Item
        $.ajax({
            url: apiUrl1,
            type: 'post',
            contentType: 'text/plain',
            data: JSON.stringify(data),
            crossDomain: true,
            processData: false,
            success: function (result) {
                alert("Simulation started! You will receive an email shortly confirming your simulation.");
                document.getElementById("simulatorSetUpForm").reset();
                location.reload();
            },
            error: function (result) {
                // show an error message
                alert("Something wrong... Try again later.");
            }
        });
    });

    $("#simulatorGetResults").submit(function (event) {
        event.preventDefault();
        var simulation_id = $("#simulation_id").val();

        var data = {simulation_id: simulation_id}

        // Call API Gateway POST Item
        $.ajax({
            url: apiUrl2,
            type: 'post',
            contentType: 'text/plain',
            data: JSON.stringify(data),
            crossDomain: true,
            processData: false,
            success: function (result) {
                $.each(result, function (i, item) {
                    $('#results-table tr:last').after('<tr><td style="font-weight:bold">' + item['day'] + '</td>' +
                        '<td>' + item['currently_infected'] + '</td>' +
                        '<td>' + item['total_infected'] + '</td>' +
                        '<td>' + item['sympt'] + '</td>' +
                        '<td>' + item['total_isolated'] + '</td>' +
                        '<td>' + item['total_dead'] + '</td></tr>');
                });
                document.getElementById("simulatorGetResults").reset();
                document.getElementById("form-content").innerHTML = '';
                document.getElementById("results-content").style.display = 'inline';
            },
            error: function (result) {
                // show an error message
                alert("Something wrong... Try again later.");
            }
        });
    });

})(jQuery);
