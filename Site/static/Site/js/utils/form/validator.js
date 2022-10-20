export const validator = () => {

$.validator.addMethod("startsWith", (text, element, param = '') => text.startsWith(param), 'Ошибка');
$.validator.addMethod("match", (text, element, param = '') => text.match(param), 'Ошибка');

};