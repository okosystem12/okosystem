import {valueList} from "./valueList";
import {linkList} from "./linkList";
import {valueGrid} from "./valueGrid";

export const materials = (data, type = 'display', ...args) => {
    switch (data?.type) {
        case 'inf':
            return valueGrid(data?.content.filter(el => el.value));
        case 'group':
            return data?.content?.name;
        case 'photo':
            return linkList(data?.content?.link || [], type, ...args);
        case 'post':
        case 'video':
            return [
                data?.content?.text,
                linkList(data?.content?.link || [], type, ...args)
            ].join(type === 'display' ? '<br>' : ', ');
        default:
            return (data) => data;
    }
};