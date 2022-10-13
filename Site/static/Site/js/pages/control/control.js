
import {prepControlForm} from "./form/prepControlForm";
import {controlForm as validateControlForm} from "../../form/validate/controlForm";
import {init} from "./table/init";
import {btnEvent} from "./work/btnEvent";

(() => {
    init();

    prepControlForm();
    validateControlForm();

    btnEvent();
})();