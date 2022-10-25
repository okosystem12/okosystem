import {doNothing} from "../../../../utils/doNothing";
import {main} from "../../../main";

export const get = (data, callback = doNothing) =>
    main('/config/place/countries/get/', data, callback, true);