export const valueGrid = (data, type = 'display') =>
    type === 'display'
        ? `<div class="simple-grid">${data?.map(el => {
            return `<b>${el.key}</b><span>${el.value}</span>`;
        }).join('')}</div>`
        : data?.map(el => `${el.key}, ${el.value}`).join(', ');