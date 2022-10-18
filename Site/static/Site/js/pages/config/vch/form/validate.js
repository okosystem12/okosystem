import {componentsData} from "../componentsData";
import {init as initHandler} from "../../../../utils/form/init";
import {submit} from "./submit";

export const validate = () => {
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
        submitHandler: submit
    });
};