import {doNothing} from "../../../utils/doNothing";
import {work} from "./work";

export const confirm = (id= null,callback=doNothing) =>
    work({id, action:'confirm'}, callback);