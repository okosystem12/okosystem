import {progress} from "../components/progress";

export const render = (render) => {
    switch (render?.type) {
        case 'progress':
            return (data, type = 'display') =>
                type === 'display'
                    ? progress(data)
                    : data;
        case 'valueList':
            return (data, type = 'display') =>
                data?.map(el =>
                    el.value
                ).join(type === 'display' ? '<br>' : ', ');
        case 'place':
            return (data, type = 'display') =>
                data?.filter(el => el)
                    .join(type === 'display' ? '<br>' : ', ');

    }
};