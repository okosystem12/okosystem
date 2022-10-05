import {userFullName} from "../../utils/user/userFullName";
import {userShortName} from "../../utils/user/userShortName";
import {bDate} from "../../utils/date/bDate";
import {phoneList} from "../../storage/control/phoneList";
import {mailList} from "../../storage/control/mailList";

export const prepControlUserList = (table, controlUserList) => {

    const columnsObj = {};

    table.columnsList.map(column => columnsObj[column.data] = '');

    return controlUserList.map(controlUser => {
        return {
            ...columnsObj,
            ...controlUser,
            fullName: userShortName(controlUser),
            birthDate: bDate(controlUser),

            phoneList: phoneList.value.filter(el => el.controlUser_id === controlUser.id),
            mailList: mailList.value.filter(el => el.controlUser_id === controlUser.id),
        }
    });
};