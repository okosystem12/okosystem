import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const inf = (data = {}, callback = doNothing) =>
    main('/archive/remove/inf/', data, callback, true);