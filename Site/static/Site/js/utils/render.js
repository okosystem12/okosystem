import {progressbar} from "../components/progressbar";
import {link} from "../components/link";

export const render = (render) => {
    switch (render?.type) {
        case 'progress':
            return (data, type = 'display') =>
                type === 'display'
                    ? progressbar(data)
                    : data?.title;
        case 'valueList':
            return (data, type = 'display') =>
                data?.map(el =>
                    el.value
                ).join(type === 'display' ? '<br>' : ', ');
        case 'place':
            return (data, type = 'display') =>
                data?.filter(el => el)
                    .join(type === 'display' ? '<br>' : ', ');

        case 'linkList':
            return (data, type = 'display') =>
                data?.map(el =>
                    type === 'display' ? link(el.href, el.value) : el.href
                ).join(type === 'display' ? '<br>' : ', ');
        default:
            return (data) => data;
    }
};