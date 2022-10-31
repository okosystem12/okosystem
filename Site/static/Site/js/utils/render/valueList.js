export const valueList = (data, type = 'display') =>
    data?.map(el => el.value).join(type === 'display' ? '<br>' : ', ');