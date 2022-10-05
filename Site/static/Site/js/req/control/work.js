import {main} from "../main";

export const work = (data, callback) =>
    main('/control/work/', data, callback);