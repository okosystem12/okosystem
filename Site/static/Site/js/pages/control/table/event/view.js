import {userId} from "../../../../storage/control/userId";
import {get} from "../../../../req/control/get";
import {openView} from "../../view/openView";
import {fillStorage} from "../../work/fillStorage";


export const view = (id) =>
    get({id}, (msg) => {
        userId.value = parseInt(id);
        fillStorage(msg);
        openView(msg.user[0]);
    });