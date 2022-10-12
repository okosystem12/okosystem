import {componentsData} from "../../pages/control/componentsData";
import {init as initHandler} from "./handler/init";
import {controlForm as submitControlForm} from "../submit/controlForm";

export const controlForm = () => {
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
        submitHandler:submitControlForm
    });
};