import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const photo = (data = {}, callback = doNothing) =>
    main('/archive/remove/photo/', data, callback, true);