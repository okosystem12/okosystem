import {loginForm as submitLoginForm} from "../submit/loginForm";
import {componentsData} from "../../pages/login/componentsData";
import {init as initHandler} from "./handler/init";

export const loginForm = () => {
    const usernameLength = 5;
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
        submitHandler: submitLoginForm
    });
};