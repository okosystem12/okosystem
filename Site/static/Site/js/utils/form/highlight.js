export const highlight = (element, text = '') => {
    const _e = $(element);
    const parent = _e.parents(".form-group");

    if (text) {
        _e.valid();
    }

    $(parent).addClass("has-error").addClass("has-feedback");

    if (!_e.is('select')) {
        _e.next("span").addClass("glyphicon-remove");
    }

    if (text) {
        $(parent).find(".help-block").html(text);
    }
};