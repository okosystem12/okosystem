import {initEvent} from "./corrupt/work/initEvent";
import {validate} from "./corrupt/form/validate";
import {init} from "./corrupt/table/init";

(() =>{
    init();
    initEvent();
    validate()
})();