import {objForEach} from "./objForEach";

export const filterListToString = (list = {}) => {
    const result = {};

    objForEach(list, (key) =>{
        result[key] = list[key]['value'];
    });

    return JSON.stringify(result)
};