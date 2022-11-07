import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const group = (data = {}, callback = doNothing) =>
    main('/archive/remove/group/', data, callback);