export const optionList = (elemList = []) =>
    [
        `<option></option>`,
        ...elemList.map(el => `<option value="${el.id}">${el.title}</option>`)
    ].join('');