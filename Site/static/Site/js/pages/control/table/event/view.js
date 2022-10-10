import {showNotificationInfo} from "../../../../utils/notification/showNotificationInfo";
import {userId} from "../../../../storage/control/userId";


export const view = (id) => {
    userId.value = parseInt(id);
    showNotificationInfo('Не работает ' + userId.value)
};