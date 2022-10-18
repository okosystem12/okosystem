import {doNothing} from "../../utils/doNothing";
import {main} from "../main";

export const get = (data, callback = doNothing) =>
    main('/corrupt/get/', data, callback, true);