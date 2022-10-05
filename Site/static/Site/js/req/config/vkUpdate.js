import {main} from "../main";

export const vkUpdate = (callback) =>
    main('/config/vk/update/', {}, callback);