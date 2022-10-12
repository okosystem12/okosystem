import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const start = (data, callback = doNothing) =>
    main('/control/search/start/', data, callback, true);