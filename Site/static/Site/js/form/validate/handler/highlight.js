export const highlight = (element, ...args) => {

    console.log(...args);
    $(element).parents(".form-group").addClass("has-error").addClass("has-feedback");
    if(!$(element).is('select')) {
        $(element).next("span").addClass("glyphicon-remove");
    }
};