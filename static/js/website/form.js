$(function () {
    var totalManageElement = $("input#id_file_set-TOTAL_FORMS");
    var currentFileCount = parseInt(totalManageElement.val());
    $("button#add-snap").on("click", function () {
        var nameElement = $("<input>", {
            type: "name",
            name: "file_set-" + currentFileCount + "-name",
            id: "id_file_set-" + currentFileCount + "-name",
        });
        var fileElement = $("<input>", {
            type: "file",
            name: "file_set-" + currentFileCount + "-src",
            id: "id_file_set-" + currentFileCount + "-src",
        });
        $("div#file-area").append(nameElement);
        $("div#file-area").append(fileElement);
        currentFileCount += 1;
        totalManageElement.attr("value", currentFileCount);
    });
});
