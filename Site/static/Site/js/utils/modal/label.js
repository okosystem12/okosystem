export const label = (elem = null, id = null, key = '', value = '') => {
    if (elem !== null) {
        elem.html(id === null ? `Добавить ${key}` : `Изменить ${key} ${value}`);
    }
};