import {transliteration} from "./transliteration/transliteration";

export const initTransliteration = (elem = null, place = null) => {
    if (elem !== null && place !== null) {
        elem.on('input', () => place.html(transliteration(elem.val())))
    }
};