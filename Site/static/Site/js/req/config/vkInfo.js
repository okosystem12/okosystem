import {main} from "../main";

export const vkInfo = (callback) =>
    main('/config/vk/info/', {}, callback);