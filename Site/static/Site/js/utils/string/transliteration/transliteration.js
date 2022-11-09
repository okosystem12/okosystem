import {transliterationDict} from "../../../var/transliterationDict";
import {transliterationKeys} from "./transliterationKeys";

export const transliteration = (string = '') =>
    string.split('').map(el => {
        if (transliterationKeys.indexOf(el) !== -1) {
            return transliterationDict[el];
        }
        else {
            return el;
        }
    }).join('');