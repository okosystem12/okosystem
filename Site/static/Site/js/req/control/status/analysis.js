import {doNothing} from "../../../utils/doNothing";
import {main} from "../../main";

export const analysis = (data, callback = doNothing) =>
    main('/control/status/analysis/', data, callback);