import {showLoad} from "../utils/load/showLoad";
import {hideLoad} from "../utils/load/hideLoad";
import {showNotificationDanger} from "../utils/notification/showNotificationDanger";
import {showNotificationWarning} from "../utils/notification/showNotificationWarning";
import {showNotificationSuccess} from "../utils/notification/showNotificationSuccess";
import {showNotificationInfo} from "../utils/notification/showNotificationInfo";
import {doNothing} from "../utils/doNothing";
import {showLoadCount} from "../storage/app/showLoadCount";

export const main = (url, data = [], callback = doNothing, silents = false) => {
    if (!silents) {
        showLoad();
        showLoadCount.value += 1;
    }

    $.ajax({
        url: url,
        method: 'POST',
        async: silents,
        data: {'data': JSON.stringify(data)},
        complete: function (msg, textStatus) {
            showLoadCount.value -= 1;
            if (textStatus === 'success') {

                try {
                    msg = JSON.parse(msg.responseText);
                }
                catch (e) {
                    msg['logout'] = true;
                }

                if(msg['logout']){
                    window.location.href = '/auth/logout/';
                    return;
                }

                if (msg.hasOwnProperty('errorText')) {
                    showNotificationDanger(msg['errorText']);
                } else if (msg.hasOwnProperty('warningText')) {
                    showNotificationWarning(msg['warningText']);
                } else if (msg.hasOwnProperty('successText')) {
                    showNotificationSuccess(msg['successText']);
                } else if (msg.hasOwnProperty('infoText')) {
                    showNotificationInfo(msg['infoText']);
                }

                callback(msg);
            }
            if (textStatus === 'error' || textStatus === 'timeout' || textStatus === 'abort') {
                showNotificationDanger('Произошла ошибка на сервере. Пожалуйста, перезагрузите страницу');
            }

            if (showLoadCount.value <= 0) {
                showLoadCount.value = 0;
                hideLoad();
            }
        }
    });
};