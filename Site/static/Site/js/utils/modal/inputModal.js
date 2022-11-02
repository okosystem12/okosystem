import {fancybox} from "../fancybox";
import {validate} from "./form/validate";

const title = '<p class="lead fancybox-confirm__title">Укажите значение</p>';
const form =
    '<form id="fancyboxConfirmForm">' +
    '<div class="form-group">' +
    '<input class="form-control" type="text" name="fancyboxVal" placeholder="">' +
    '</div>' +
    '<button type="submit" class="btn btn-success fancybox-confirm__btn"><span class="btn-label"><span class="glyphicon glyphicon-ok"></span></span>' +
    'Подтвердить</button>' +
    '<button type="button" class="btn btn-danger fancybox-confirm__btn" id="fancyboxConfirmClose">' +
    '<span class="btn-label"><span class="glyphicon glyphicon-remove"></span></span>' +
    'Отмена</button></form>';

export const inputModal = (text = '', value = '', callback) =>
    $.fancybox.open({
        src: `<div class="fancybox-confirm">${title}${form}</div>`,
        type: "html",
        opts: {
            ...fancybox,
            afterShow: () => {
                const fancyboxConfirmForm = $('#fancyboxConfirmForm');
                const input = fancyboxConfirmForm.find('.form-control');

                input.val(value);
                input.attr('placeholder', text);

                validate(fancyboxConfirmForm, callback);

                $('#fancyboxConfirmClose')
                    .off('click')
                    .on('click', (e) => {
                        e.preventDefault();
                        $.fancybox.close();
                    });
            }
        },
    });