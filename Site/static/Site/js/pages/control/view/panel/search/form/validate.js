import {init as initHandler} from "../../../../../../utils/form/init";
import {submit} from "./submit";

export const validate = (form) => {
    $(form).validate({
        rules: {
            socialValue: {
                normalizer: $.trim,
                required: true,
                url: true,
                match: /^https?:\/\/vk\.com\/id.+/,
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