import {fancybox} from "../fancybox";
import {validate} from "./form/validate";
import {initChosen} from "../list/initChosen";
import {initOptionList} from "../../components/select/initOptionList";

const title = '<p class="lead fancybox-confirm__title">Укажите значение</p>';
const form = (multiple = false) =>
    '<form id="fancyboxConfirmForm">' +
    '<div class="form-group">' +
    `<select class="form-control" name="fancyboxVal" ${multiple ? 'multiple' : ''}></select>` +
    '</div>' +
    '<button type="submit" class="btn btn-success fancybox-confirm__btn"><span class="btn-label"><span class="glyphicon glyphicon-ok"></span></span>' +
    'Подтвердить</button>' +
    '<button type="button" class="btn btn-danger fancybox-confirm__btn" id="fancyboxConfirmClose">' +
    '<span class="btn-label"><span class="glyphicon glyphicon-remove"></span></span>' +
    'Отмена</button></form>';

export const selectModal = (text = '', value = '', multiple = false, valueList = [], callback) =>
    $.fancybox.open({
        src: `<div class="fancybox-confirm">${title}${form(multiple)}</div>`,
        type: "html",
        opts: {
            ...fancybox,
            afterShow: () => {
                const fancyboxConfirmForm = $('#fancyboxConfirmForm');
                const select = fancyboxConfirmForm.find('.form-control');

                initChosen(select);
                initOptionList(select, valueList, value);

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