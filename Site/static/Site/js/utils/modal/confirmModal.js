import {fancybox} from "../fancybox";

const title = '<p class="lead fancybox-confirm__title">Подтвердите действие</p>';
const btn =
    '<button type="button" class="btn btn-success fancybox-confirm__btn" id="fancyboxConfirmSubmit">' +
    '<span class="btn-label"><span class="glyphicon glyphicon-ok"></span></span>' +
    'Подтвердить</button>' +
    '<button type="button" class="btn btn-danger fancybox-confirm__btn" id="fancyboxConfirmReject">' +
    '<span class="btn-label"><span class="glyphicon glyphicon-remove"></span></span>' +
    'Отмена</button>';

export const confirmModal = (text = '', callback) =>
    $.fancybox.open({
        src: `<div class="fancybox-confirm">${title}<p class="fancybox-confirm__text">${text}</p>${btn}</div>`,
        type: "html",
        opts: {
            ...fancybox,
            afterShow: () => {
                $('#fancyboxConfirmSubmit')
                    .off('click')
                    .on('click', (e) => {
                        e.preventDefault();
                        $.fancybox.close();
                        if(callback) {
                            callback();
                        }
                    });
                $('#fancyboxConfirmReject')
                    .off('click')
                    .on('click', (e) => {
                        e.preventDefault();
                        $.fancybox.close();
                    });
            }
        },
    });