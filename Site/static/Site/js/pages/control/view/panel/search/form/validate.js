import {init as initHandler} from "../../../../../../utils/form/init";
import {submit} from "./submit";
import {socialPrefix} from "../../../../../../var/socialPrefix";

export const validate = (form) => {
    const allOther = '.+';
    $(form).validate({
        rules: {
            socialValue: {
                normalizer: $.trim,
                required: true,
                url: true,
                match: new RegExp(socialPrefix + allOther),
            },
        },
        messages: {
            socialValue: {
                required: `Укажите ссылку`,
                url: `Укажите корректную ссылку`,
                match: `Укажите корректную ссылку на профиль`,
            },
        },
        ...initHandler,
        submitHandler: submit
    });
};