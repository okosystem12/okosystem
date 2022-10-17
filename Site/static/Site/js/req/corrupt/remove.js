import {main} from "../main";
import {doNothing} from "../../utils/doNothing";

export const remove = (data, callback = doNothing) =>
    main('/corrupt/remove/', data, callback);