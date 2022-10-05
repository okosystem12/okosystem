import {main} from "./main";

export const authLogin = (data, callback) =>
    main('/auth/login/', data, callback);