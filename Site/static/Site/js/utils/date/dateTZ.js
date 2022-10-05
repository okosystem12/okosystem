export const dateTZ = (date) =>
    new Date(date.setMinutes(date.getMinutes() - date.getTimezoneOffset()));