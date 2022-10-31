import {doNothing} from "../../utils/doNothing";
import {main} from "../main";

export const get = (data, callback = doNothing) =>
    main('/config/vch/get/', data, callback, true);