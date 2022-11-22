import {get} from "../../../../req/corrupt/get";
import {openForm} from "../../form/openForm";
import {showNotificationWarning} from "../../../../utils/notification/showNotificationWarning";

export const edit = (id) =>
    get({id}, (msg) =>
        openForm(msg.corrupt[0]));