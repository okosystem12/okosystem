export const place = (data, type = 'display') =>
    data?.filter(el => el)
        .join(type === 'display' ? '<br>' : ', ');