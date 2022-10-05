import {authLogin} from "../../req/authLogin";
import {highlight} from "../validate/handler/highlight";
import {componentsData} from "../../pages/login/componentsData";

export const loginForm = (form, e) => {
    e.preventDefault();
    const {username, password} = componentsData;
    const path = window.location.pathname;

    authLogin({
        username: username.val().trim(),
        password: password.val().trim(),
        path
    }, (msg) => {
        if (msg.hasOwnProperty('redirect')) {
            window.location.href = msg.redirect;
        }
        else {
            highlight(username);
            highlight(password);
        }
    })
};