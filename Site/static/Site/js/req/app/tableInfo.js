import {main} from "../main";

export const tableInfo = (data, callback) =>
    main('/table/info/', data, callback);