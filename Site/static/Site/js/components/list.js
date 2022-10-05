export const list = (elemList) =>
    `<ul>${
        elemList.map(elem => `<li>${elem}</li>`).join('')
        }</ul>`;