import {doNothing} from "../../utils/doNothing";
import {main} from "../main";

export const get = (data, callback = doNothing) =>
    main('/control/get/', data, callback);