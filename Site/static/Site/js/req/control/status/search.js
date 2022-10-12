import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const search = (data, callback = doNothing) =>
    main('/control/status/search/', data, callback, true);