import {main} from "../../main";
import {doNothing} from "../../../utils/doNothing";

export const info = (data = {}, callback = doNothing) =>
    main('/config/place/info/', data, callback);