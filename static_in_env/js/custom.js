// Auto close messages

$(function () {
    TriggerAlertClose();
});

function TriggerAlertClose() {
    window.setTimeout(function () {
        $(".alert").fadeTo(1000, 0).slideUp(1000, function () {
            $(this).remove();
        });
    }, 3000);
}
//  Delete Timer Modal
$(document).on('click', '.confirm-delete', function () {
    $("#confirmTimerDeleteModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmDeleteTimerButtonModal', function () {
    var caller = $("#confirmDeleteTimerButtonModal").closest(".modal").attr("caller-id");
    window.location = $("#".concat(caller)).attr("href");
});
// Bootstrap Tooltip
$(function () {
    $('[tooltip-toggle="tooltip"]').tooltip()
})