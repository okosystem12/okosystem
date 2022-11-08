import {main} from "../../main";

export const archive = (callback) =>
    main('/index/statistics/archive/', {}, callback);