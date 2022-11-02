import {inputModal} from "../../modal/inputModal";
import {doNothing} from "../../doNothing";

export const input = (table = {}, text = '', key = '', value = {}) => {
    return {
        text,
        action: (e, dt, node, config, action = doNothing) => {
            inputModal(
                text,
                table.filter[key] ? table.filter[key]['value'] : '',
                (inputValue = '') => {
                    if(inputValue !== '') {
                        value['value'] = inputValue;
                        value['text'] = inputValue;
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