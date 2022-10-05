import {showLoad} from "../utils/load/showLoad";
import {hideLoad} from "../utils/load/hideLoad";
import {showNotificationDanger} from "../utils/notification/showNotificationDanger";
import {showNotificationWarning} from "../utils/notification/showNotificationWarning";
import {showNotificationSuccess} from "../utils/notification/showNotificationSuccess";
import {showNotificationInfo} from "../utils/notification/showNotificationInfo";
import {doNothing} from "../utils/doNothing";

export const main = (url, data = [], callback = doNothing, silents = false) => {
    if (!silents) {
        showLoad();
    }

    $.ajax({
        url: url,
        method: 'POST',
        async: silents,
        data: {'data': JSON.stringify(data)},
        complete: function (msg, textStatus) {
            if (textStatus === 'success') {

                msg = JSON.parse(msg.responseText);

                if (msg.hasOwnProperty('errorText')) {
                    showNotificationDanger(msg['errorText']);
                } else if (msg.hasOwnProperty('warningText')) {
                    showNotificationWarning(msg['warningText']);
                } else if (msg.hasOwnProperty('successText')) {
                    showNotificationSuccess(msg['successText']);
                } else if (msg.hasOwnProperty('infoText')) {
                    showNotificationInfo(msg['infoText']);
                }

                if (callback) {
                    callback(msg);
                }

                hideLoad();
            }
            if (textStatus === 'error' || textStatus === 'timeout' || textStatus === 'abort') {
                showNotificationDanger('Произошла ошибка на сервере. Пожалуйста, перезагрузите страницу');
                hideLoad();
            }
        }
    });
};