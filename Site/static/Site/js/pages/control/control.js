
import {prepControlForm} from "./form/prepControlForm";
import {controlForm as validateControlForm} from "../../form/validate/controlForm";
import {btnAddEvent} from "./work/btnAddEvent";
import {init} from "./table/init";

(() => {
    init();

    prepControlForm();
    validateControlForm();

    btnAddEvent();
})();