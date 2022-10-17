export const unhighlight = (element) => {
    $(element).parents(".form-group").removeClass("has-error").removeClass("has-feedback");
    if (!$(element).is('select')) {
        $(element).next("span").removeClass("glyphicon-remove");
    }
};