import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const get = (callback = doNothing) =>
    main('/config/token/get/', {}, callback);