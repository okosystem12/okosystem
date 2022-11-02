import {option} from "./option";
import {optgroup} from "./optgroup";

export const optionList = (elemList = []) => {
    const result = ['<option></option>'];

    const notGrouped = elemList.filter(el => el.group === undefined);
    const grouped = elemList.filter(el => el.group !== undefined);
    const groupList = [];

    notGrouped.forEach(el => result.push(option(el)));

    grouped.forEach(el => groupList.indexOf(el.group) === -1 ? groupList.push(el.group) : []);

    groupList.forEach(el => result.push(optgroup(el, grouped.filter(o=> o.group === el).map(o => option(o)).join(''))));


    return result.join('');
};
