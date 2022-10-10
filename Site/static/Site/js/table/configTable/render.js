export const render = (render) => {
    switch (render?.type) {
        case 'progress':
            return (data, type, row, meta) =>
                type === 'display'
                    ? `<progress value="${data}" max="${render.max}"></progress>`
                    : data;
        case 'date':
            return DataTable.render.date();
        case 'datetime':
            return DataTable.render.datetime();
        case 'valueList':
            return (data, type, row, meta) =>
                data?.map(el =>
                    el.value
                ).join(type === 'display' ? '<br>' : ', ');
        case 'place':
            return (data, type, row, meta) =>
                data?.filter(el => el)
                    .join(type === 'display' ? '<br>' : ', ');

    }
};