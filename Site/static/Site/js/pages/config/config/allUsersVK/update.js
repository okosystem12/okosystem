import {eventUpdate} from "./eventUpdate";
import {allUsersVK} from "../../../../storage/config/allUsersVK";
import {componentsData} from "../componentsData";
import {loader} from "../../../../components/loader";
import {dateFormat} from "../../../../utils/date/dateFormat";

export const update = () => {
    const {updateAllUsersVK, dateAllUsersVK} = componentsData;

    updateAllUsersVK.removeAttr('disabled');

    if (allUsersVK.value) {
        if (allUsersVK.value.dateEnd === null) {
            dateAllUsersVK.html(loader('Ожидайте завершения обновления'));
            updateAllUsersVK.attr('disabled', 'disabled');
        }
        else {
            dateAllUsersVK.html(dateFormat(allUsersVK.value.dateEnd));
        }
    }
    else {
        dateAllUsersVK.html('Обновлений не производилось');
    }
    eventUpdate();
};