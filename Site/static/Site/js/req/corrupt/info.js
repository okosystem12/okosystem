import {main} from "../main";
import {doNothing} from "../../utils/doNothing";

export const info = (callback = doNothing) =>
    main('/corrupt/info/', {}, callback);