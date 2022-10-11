import {userId} from "../../../../storage/control/userId";
import {openForm} from "../../form/openForm";
import {get} from "../../../../req/control/get";
import {fillStorage} from "../../work/fillStorage";

export const edit = (id) =>
    get({id}, (msg) => {
        userId.value = parseInt(id);
        fillStorage(msg);
        openForm(msg.user[0]);
    });