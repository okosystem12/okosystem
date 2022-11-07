import {main} from "../main";

export const login = (data, callback) =>
    main('/auth/login/', data, callback);