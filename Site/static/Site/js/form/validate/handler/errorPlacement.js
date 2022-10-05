export const errorPlacement = (error, element) => {
    error.addClass("help-block");
    element.parents(".form-group").addClass("has-feedback");

    if (element.prop("type") === "checkbox") {
        error.insertAfter(element.parent("label"));
    }
    else if (element.is('select')) {
        element.parents(".form-group").append(error);
    }
    else {
        error.insertAfter(element);
    }

    if(!element.is('select')) {
        if (!element.next("span")[0]) {
            $("<span class='glyphicon glyphicon-remove form-control-feedback'></span>").insertAfter(element);
        }
    }
};