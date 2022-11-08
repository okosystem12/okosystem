
import {prepControlForm} from "./control/form/prepControlForm";
import {validate} from "./control/form/validate";
import {init} from "./control/table/init";
import {btnEvent} from "./control/work/btnEvent";

(() => {
    init();
    prepControlForm();
    validate();
    btnEvent();
})();