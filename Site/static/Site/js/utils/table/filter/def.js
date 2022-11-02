import {doNothing} from "../../doNothing";

export const def = (table = {}, text = '', key = '', value = {}) => {
    return {
        text,
        action: (e, dt, node, config, action = doNothing) => {
            table.filter[key] = value;
            action();
        }
    }
};
