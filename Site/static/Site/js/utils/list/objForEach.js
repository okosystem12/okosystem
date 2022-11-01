import {doNothing} from "../doNothing";

export const objForEach = (obj = {}, callback = doNothing) => {
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            callback(key);
        }
    }
};