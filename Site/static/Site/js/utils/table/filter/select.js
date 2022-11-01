import {doNothing} from "../../doNothing";
import {selectModal} from "../../modal/selectModal";

export const select = (table = {}, text = '', key = '', value = {}, valueList = []) => {
    return {
        text,
        action: (e, dt, node, config, action = doNothing) => {
            selectModal(
                text,
                table.filter[key] ? table.filter[key]['value'] : '',
                valueList,
                (selectValue = '') => {
                    selectValue = selectValue.split(',').filter(el => el !== '').map(el => parseInt(el));

                    if(selectValue.length){
                        value['value'] = selectValue;
                        value['text'] = valueList.filter(el => selectValue.indexOf(el.id) !== -1).map(el => el.title).join(', ');
                        table.filter[key] = value;
                    }
                    else {
                        delete table.filter[key];
                    }

                    action();
                });
        }
    }
};