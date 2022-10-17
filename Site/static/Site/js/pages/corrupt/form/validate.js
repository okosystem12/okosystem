import {componentsData} from "../componentsData";
import {init as initHandler} from "../../../utils/form/init";
import {submit as submitCorruptForm} from "../../../pages/corrupt/form/submit";

export const validate  = () => {
    const corruptValueLength = 2;
    const {corruptForm} = componentsData;

    corruptForm.validate({
        rules: {
            corruptValue: {
                required: true,
                minlength: corruptValueLength,
                normalizer: $.trim
            },

        },
        messages: {
            corruptValue: {
                required: `Пожалуйста укажите ключевое слово`,
                minlength: `Ключевое слово должно содержать не менее ${corruptValueLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submitCorruptForm
    });
};