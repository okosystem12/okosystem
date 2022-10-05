import {componentsData} from "../../pages/config/vch/componentsData";
import {init as initHandler} from "./handler/init";
import {vchForm as submitVchForm} from "../submit/vchForm";

export const vchForm = () => {
    const vchNumberLength = 2;
    const {vchForm} = componentsData;

    vchForm.validate({
        rules: {
            vchNumber: {
                required: true,
                minlength: vchNumberLength,
                normalizer: $.trim
            },

        },
        messages: {
            vchNumber: {
                required: `Пожалуйста укажите номер ВЧ`,
                minlength: `Номер ВЧ должен содержать не менее ${vchNumberLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submitVchForm
    });
};