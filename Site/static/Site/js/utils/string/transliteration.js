import {transliterationDict, transliterationKeys} from "../../var/transliterationDict";

export const transliteration = (string = '') =>
    string.split('').map(el => {
        if (transliterationKeys.indexOf(el) !== -1) {
            return transliterationDict[el];
        }
        else {
            return el;
        }
    }).join('');