import {eventUpdate} from "./eventUpdate";
import {componentsData} from "../componentsData";
import {loader} from "../../../../components/loader";
import {dateFormat} from "../../../../utils/date/dateFormat";

export const update = (allUsersVK = null) => {
    const {updateAllUsersVK, dateAllUsersVK} = componentsData;

    updateAllUsersVK.removeAttr('disabled');

    if (allUsersVK) {
        if (allUsersVK.dateEnd === null) {
            dateAllUsersVK.html(loader('Ожидайте завершения обновления'));
            updateAllUsersVK.attr('disabled', 'disabled');
        }
        else {
            dateAllUsersVK.html(dateFormat(allUsersVK.dateEnd));
        }
    }
    else {
        dateAllUsersVK.html('Обновлений не производилось');
    }
    eventUpdate();
};