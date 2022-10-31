import {valueList} from "./valueList";
import {progress} from "./progress";
import {place} from "./place";
import {linkList} from "./linkList";
import {materials} from "./materials";


export const render = (render) => {
    switch (render?.type) {
        case 'progress':
            return (data, type = 'display', ...args) => progress(data || {}, type, ...args);
        case 'valueList':
            return (data, type = 'display', ...args) => valueList(data || [], type, ...args);
        case 'place':
            return (data, type = 'display', ...args) => place(data || [], type, ...args);
        case 'linkList':
            return (data, type = 'display', ...args) => linkList(data || [], type, ...args);
        case 'materials':
            return (data, type = 'display', ...args) => materials(data || {}, type, ...args);
        default:
            return (data) => data;
    }
};