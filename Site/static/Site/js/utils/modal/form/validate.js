import {init as initHandler} from "../../../utils/form/init";
import {submit} from "./submit";
import {doNothing} from "../../doNothing";

export const validate = (form, callback = doNothing) => {

    form.validate({
        rules: {
            fancyboxVal: {
                // required: true,
                normalizer: $.trim
            },
        },
        messages: {
            fancyboxVal: {
                required: `Это поле обязательно для заполнения`
            },
        },
        ...initHandler,
        submitHandler: (form, e) => submit(form, e, callback)
    });
};