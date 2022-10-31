export const accordionParent = (id = '', content = '') =>
    `<div class="panel-group" id="${id}" role="tablist" aria-multiselectable="true">${content}</div>`;