import {componentsData} from "../componentsData";
import {init as initHandler} from "../../../../utils/form/init";
import {submit} from "./submit";

export const validate = () => {
    const {tokenForm} = componentsData;

    tokenForm.validate({
        rules: {
            tokenInput: {
                required: true,
                normalizer: $.trim
            },
        },
        messages: {
            tokenInput: {
                required: `Пожалуйста укажите токен администратора`
            },
        },
        ...initHandler,
        submitHandler: submit
    });
};