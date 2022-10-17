export const success = (label, element) => {
    if (!$(element).is('select')) {
        if (!$(element).next("span")[0]) {
            $("<span class='glyphicon glyphicon-ok form-control-feedback'></span>").insertAfter($(element));
        }
    }
};