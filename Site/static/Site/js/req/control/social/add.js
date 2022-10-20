import {doNothing} from "../../../utils/doNothing";
import {work} from "./work";

export const add = () => (value = '', callback = doNothing) =>
    work({value, action: 'add'}, callback);