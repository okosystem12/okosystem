export const row = (el = {title: '', value: ''}) =>
    `
<div class="statistics-grid__row">${el.title}</div>
<div class="statistics-grid__value">${el.value || ''}</div>
`;