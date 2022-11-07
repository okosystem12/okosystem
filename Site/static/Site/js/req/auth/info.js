import {main} from "../main";

export const info = (callback) =>
    main('/auth/info/', {}, callback);