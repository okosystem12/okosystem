import {main} from "../main";

export const info = (callback) =>
    main('/control/info/', {}, callback);