import {initEvent} from "./work/initEvent";
import {validate} from "./form/validate";
import {init} from "./table/init";

(() =>{
    init();
    initEvent();
    validate()
})();