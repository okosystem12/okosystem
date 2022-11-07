import {info} from "../../req/auth/info";
import {user} from "../../storage/user";
import {setName} from "./setName";

export const userInfo = () =>
    info((msg) => {
        user.value = msg.user;
        setName();
    });