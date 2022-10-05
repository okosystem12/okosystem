import {controlUserList} from "../../../../storage/control/controlUserList";
import {controlUserImgList} from "../../../../storage/control/controlUserImgList";
import {phoneList} from "../../../../storage/control/phoneList";
import {mailList} from "../../../../storage/control/mailList";
import {remove as reqRemove} from "../../../../req/control/remove";
import {removeRowById} from "../../../../table/handler/removeRowById";
import {table} from "../../../../storage/control/table";

export const remove = (id) => {
    controlUserList.remove('id', id);
    controlUserImgList.remove('controlUser_id', id);
    phoneList.remove('controlUser_id', id);
    mailList.remove('controlUser_id', id);
    reqRemove({id});
    removeRowById(table.value.table, id);
};