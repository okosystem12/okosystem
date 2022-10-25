import {submit} from "./submit";
import {componentsData} from "../componentsData";
import {init as initHandler} from "../../../utils/form/init";

export const validate = () => {
    const usernameLength = 3;
    const passwordLength = 6;
    const {loginForm} = componentsData;

    loginForm.validate({
        rules: {
            username: {
                required: true,
                minlength: usernameLength,
                normalizer: $.trim
            },
            password: {
                required: true,
                minlength: passwordLength,
                normalizer: $.trim
            },
        },
        messages: {
            username: {
                required: `Пожалуйста укажите свой логин`,
                minlength: `Ваш логин должен содержать не менее ${usernameLength} символов`
            },
            password: {
                required: `Пожалуйста укажите свой пароль`,
                minlength: `Ваш пароль должен содержать не менее ${passwordLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submit
    });
};