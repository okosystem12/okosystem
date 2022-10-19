import {doNothing} from "../../../utils/doNothing";
import {work} from "./work";

export const reject = (id = null, callback = doNothing) =>
    work({id, action: 'reject'}, callback);