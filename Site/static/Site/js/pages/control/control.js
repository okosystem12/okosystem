
import {prepControlForm} from "./form/prepControlForm";
import {validate} from "./form/validate";
import {init} from "./table/init";
import {btnEvent} from "./work/btnEvent";

(() => {
    init();
    prepControlForm();
    validate();
    btnEvent();
})();