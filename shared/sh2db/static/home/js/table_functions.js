/*global showAlert*/

function checkbox_selection () {
    $("#alignment_table > tbody > tr").click(function(event) {
        if (event.target.type !== "checkbox") {
            $(":checkbox", this).trigger("click");
            $(this).eq(0).toggleClass("alt_selected");
        }
        $(this).eq(0).toggleClass("alt_selected");
    });

    $("#select-all").click(function() {
        $(":checkbox", this).trigger("click");
        if ($(this).prop("checked")===true) {
            $(".alt:visible").prop("checked", true);
            $(".alt:visible").parent().parent().addClass("alt_selected");
        }
        if ($(this).prop("checked")===false) {
            $(".alt:visible").prop("checked", false);
            $(".alt:visible").parent().parent().removeClass("alt_selected");
        }
    });
}

function alignment_download () {
    $("#alignment_download_button").click(function() {
        var dataCSV = '';
        if ($(".alt_selected").length===0 || ($(".alt_selected").length===1 & $("#select-all").parent().parent().hasClass("alt_selected"))) {
            showAlert("No entries selected", "danger");
        }
        else {
            $("#alignment_table tr").each(function() {
                if ($(this).is(':first-child') || $(this).hasClass("alt_selected")) {
                    $(this).find("th").each(function(key, cell) {
                        dataCSV += $(cell).text()+",".repeat($(cell).prop("colSpan"));
                    })
                    $(this).find("td").each(function(key, cell) {
                        dataCSV += $(cell).text()+",";
                    })
                    dataCSV += "\n";
                }
            })
            var hiddenElement = document.createElement('a');  
            hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(dataCSV);  
            hiddenElement.target = '_blank';  
            hiddenElement.download = 'SH2DB_alignment.csv';  
            hiddenElement.click();
        }
    });
}

function structure_download () {
    $("#structure_download_button").click(function() {
        var structures = [];
        if ($(".structure.alt_selected").length===0) {
            showAlert("No structure entries selected", "danger");
        }
        else {
            $(".structure.alt_selected").each(function() {
                structures.push($(":nth-child(3)", this).text());
            });
            // StructureDownload(structures.join(','));
            window.location.href = '/structure/download?ids='+structures.join(",");
        }
    });
}

function StructureDownload (structures) {
    $.ajax({
        'url': '/structure/download',
        'data': {"structures": structures},
        'type': 'GET',
        'success': function(response) {},
        'error': function(response) {}
    });
}

function table_filter () {
    fill_filter(".protein", "#protein_filter");
    fill_filter(".domain", "#domain_filter");
    for (var i=1; i<$(".data-row:first > .residue").length+1; i++) {
        fill_filter(".res_"+i.toString(), "#filter_"+i.toString())
    }
    run_filter();
}

function run_filter () {
    $("select").change(function() {
        var selected = $(this).find(":selected").text();
        if ($(this).attr("id")==="protein_filter")  {
            var column = $(".protein");
        }
        else if ($(this).attr("id")==="domain_filter") {
            var column = $(".domain");
        }
        else {
            var column = $(".res_"+$(this).attr("id").split("_")[1]);
        }
        $(column).each(function (key, val) {
            if (selected.toString()!==$(val).text()) {
                $(this).parent().hide();
            }
            if (selected.toString()==="") {
                if ($("#structure_toggle_button").hasClass("left_position")) {
                    if (!$(this).parent().hasClass("structure")) {
                        $(this).parent().show();
                    }
                }
                else {
                    $(this).parent().show();
                }
            }
        })
    });
}

function fill_filter (td_class, filter_id) {
    var options = [];
    $(td_class).each(function (key, val) {
        if (!options.includes(val.innerHTML)) {
            options.push(val.innerHTML);
        }
    });
    $(filter_id).append(`<option value=""></option>`)
    $(options).each(function (key, val) {
        $(filter_id).append(`<option value="${val}">${val}</option>`);
    });
}