import {authLogin} from "../../../req/authLogin";
import {highlight} from "../../../utils/form/highlight";
import {componentsData} from "../componentsData";

export const submit = (form, e) => {
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
            if (msg.errorUsernameHighlight) {
                highlight(username, msg.errorUsernameHighlight);
            }
            if (msg.errorPasswordHighlight) {
                highlight(password, msg.errorPasswordHighlight);
            }
        }
    })
};