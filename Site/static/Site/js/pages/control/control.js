
import {prepControlForm} from "./form/prepControlForm";
import {controlForm as validateControlForm} from "../../form/validate/controlForm";
import {btnAddEvent} from "./work/btnAddEvent";
import {init} from "./table/init";
import {transliteration} from "../../utils/string/transliteration";

(() => {
    init();

    prepControlForm();
    validateControlForm();

    btnAddEvent();

    console.log(transliteration('Михаил'));
})();