import {componentsData} from "../componentsData";
import {init as initHandler} from "../../../utils/form/init";
import {submit} from "../../../pages/control/form/submit";

export const validate = () => {
    const {controlForm} = componentsData;

    controlForm.validate({
        rules: {
            firstName: {
                required: true,
                normalizer: $.trim
            },
            lastName: {
                required: true,
                normalizer: $.trim
            },
            birthDate: {
                required: true,
                normalizer: $.trim
            },
        },
        messages: {
            firstName: {
                required: `Укажите имя`
            },
            lastName: {
                required: `Укажите фамилию`
            },
            birthDate: {
                required: `Укажите дату рождения`
            },
        },
        ...initHandler,
        submitHandler:submit
    });
};