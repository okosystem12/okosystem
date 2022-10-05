import {showNotificationInfo} from "../../../../utils/notification/showNotificationInfo";
import {userId} from "../../../../storage/control/userId";
import {controlUserList} from "../../../../storage/control/controlUserList";


export const view = (id) => {
    userId.value = parseInt(id);
    const user = controlUserList.value.find(user => user.id === userId.value);
    showNotificationInfo('Не работает ' + user.firstName)
};