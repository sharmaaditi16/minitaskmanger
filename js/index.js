$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:5000/tasks",
        method: "GET",
        success: function (response) {
            let tasks = response.tasks;
            for (let i = 0; i < tasks.length; i++) {
                let task = tasks[i];
                $("tbody").append("<tr><td>" + task.id + "</td>" +
                    "<td>" + task.title + "</td>" +
                    "<td>" + task.description + "</td>" +
                    "<td>" + task.due_date + "</td>" +
                    "<td>" + (task.created_at || "-") + "</td>" +
                    "<td><a href='edit-task.html?task=" + task.id + "' target='_blank' class='btn btn-secondary'>Edit</a> " +
                    "<input type='button' value='Delete' class='btn btn-danger delete-btn' custom-id='task" + task.id + "'></td></tr>");
                $("body").append("<input type='hidden' value='" + task.id + "' id='task" + task.id + "'>");
            }

            // Attach delete click handler
            $(".delete-btn").click(function () {
                var taskId = $(this).attr('custom-id');
                var actualTaskId = $('#' + taskId).val();
                var apiUrl = "http://127.0.0.1:5000/tasks/" + actualTaskId;

                $.ajax({
                    url: apiUrl,
                    method: 'DELETE',
                    contentType: 'application/json',
                    success: (response) => {
                        console.log(response.message);
                        $(this).removeAttr("custom-id");
                        $(this).closest("tr").fadeOut();
                    }
                });
            });
        }
    })
});
