export const elem = (el = {title: '', value: ''}) =>
    `
<div class="statistics-grid__title">${el.title}</div>
<div class="statistics-grid__value">${el.value}</div>
`;