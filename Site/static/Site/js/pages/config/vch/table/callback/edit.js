import {get} from "../../../../../req/config/vch/get";
import {openForm} from "../../form/openForm";

export const edit = (id) =>
    get({id}, (msg) => openForm(msg.vch[0]));