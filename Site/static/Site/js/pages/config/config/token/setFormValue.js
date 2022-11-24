import {componentsData} from "../componentsData";

export const setFormValue = (data = {}) =>
    componentsData.tokenInput.val(data.tokenVK || '');