import {main} from "../../main";

export const corrupt = (callback) =>
    main('/index/statistics/corrupt/', {}, callback);