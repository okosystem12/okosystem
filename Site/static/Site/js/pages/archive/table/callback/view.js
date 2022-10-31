import {userId} from "../../../../storage/control/userId";
import {get} from "../../../../req/archive/get";


export const view = (id) =>
    get({id}, (msg) => {
        userId.value = parseInt(id);
    });