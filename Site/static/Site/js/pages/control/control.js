
import {prepControlForm} from "./form/prepControlForm";
import {controlForm as validateControlForm} from "../../form/validate/controlForm";
import {init} from "./table/init";
import {transliteration} from "../../utils/string/transliteration";
import {btnEvent} from "./work/btnEvent";

(() => {
    init();

    prepControlForm();
    validateControlForm();

    btnEvent()

    console.log(transliteration('Имя'));
    console.log(transliteration('Отчество'));
})();